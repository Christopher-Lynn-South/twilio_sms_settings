from odoo import models, fields, _
from twilio.rest import Client
import threading
import logging

_logger = logging.getLogger(__name__)


class TwilioSMS(models.Model):
    _inherit = 'sms.sms'

    error_message = fields.Text('Error Message', copy=False, readonly=1)

    def send(self, delete_all=False, auto_commit=False, raise_exception=False):
        """ Main API method to send SMS.

          :param delete_all: delete all SMS (sent or not); otherwise delete only
            sent SMS;
          :param auto_commit: commit after each batch of SMS;
          :param raise_exception: raise if there is an issue contacting IAP;
        """
        is_message_overwrite = self.env['ir.config_parameter'].sudo().get_param(
            'ql_scheduler_reminder.twilio_overrwrite_odoo_sms') == 'True'
        
        # Log the overwrite setting for debugging
        _logger.info(f"Twilio SMS Overwrite setting: {is_message_overwrite}")
            
        for batch_ids in self._split_batch():
            if not is_message_overwrite:
                _logger.info(f"Using standard Odoo SMS for batch {batch_ids}")
                self.browse(batch_ids)._send(delete_all=delete_all, raise_exception=raise_exception)
            else:
                _logger.info(f"Using Twilio SMS for batch {batch_ids}")
                self.browse(batch_ids).twilio_send_sms()
                
            # auto-commit if asked except in testing mode
            if auto_commit is True and not getattr(threading.current_thread(), 'testing', False):
                self._cr.commit()

    def twilio_send_sms(self, delete_all=False, raise_exception=False):
        param_obj = self.env['ir.config_parameter']
        twilio_account_sid = param_obj.sudo().get_param('ql_scheduler_reminder.twilio_account_sid')
        twilio_auth_token = param_obj.sudo().get_param('ql_scheduler_reminder.twilio_auth_token')
        twilio_from_number = param_obj.sudo().get_param('ql_scheduler_reminder.twilio_from_number')

        if not all([twilio_account_sid, twilio_auth_token, twilio_from_number]):
            error_msg = 'Twilio configuration incomplete. Please check settings.'
            _logger.error(error_msg)
            self.write({'state': 'error', 'error_message': error_msg})
            return

        client = Client(twilio_account_sid, twilio_auth_token)

        for rec_id in self:
            phone = rec_id.number
            try:
                _logger.info(f"Sending Twilio SMS to {phone}")
                response = client.messages.create(body=rec_id.body, from_=twilio_from_number, to=phone)
                
                _logger.info(f"Twilio response SID: {response.sid}")
                
                # Check for error in response
                if hasattr(response, 'error_code') and response.error_code:
                    state = 'error'
                    error_message = f"Error {response.error_code}: {response.error_message}"
                    _logger.error(error_message)
                else:
                    state = 'sent'
                    error_message = None
                    
            except Exception as e:
                state = 'error'
                error_message = str(e)
                _logger.exception(f"Twilio SMS sending failed: {error_message}")
                
            rec_id.write({'error_message': error_message, 'state': state})
