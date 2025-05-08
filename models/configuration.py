from odoo import fields, models, api, _


class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    twilio_account_sid = fields.Char('Account SID', config_parameter='ql_twilio_sms.account_sid')
    twilio_auth_token = fields.Char('Authentication Token', config_parameter='ql_twilio_sms.auth_token')
    twilio_from_number = fields.Char('Phone Number', config_parameter='ql_twilio_sms.from_number')
    twilio_overwrite_odoo_sms = fields.Boolean('Overwrite Odoo SMS', config_parameter='ql_twilio_sms.overwrite_odoo_sms')
