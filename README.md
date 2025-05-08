# Twilio SMS Integration for Odoo 18

This module integrates Twilio's SMS service with Odoo 18, allowing you to send SMS messages directly through Twilio instead of the default Odoo IAP SMS service.

## Features

- Configure Twilio credentials in Odoo settings
- Send SMS messages using Twilio's API
- Option to override Odoo's default SMS functionality
- Detailed error reporting for failed SMS messages
- Compatible with Odoo 18 Community and Enterprise editions

## Installation

### Prerequisites

- Odoo 18.0
- Python 3.8+
- Twilio Python library (`twilio`)

### Steps

1. Install the Twilio Python package:
   ```bash
   pip3 install twilio
   ```

2. Download the module and place it in your Odoo addons directory:
   ```bash
   cd /path/to/your/odoo/addons
   git clone https://github.com/yourusername/ql_twilio_sms.git
   # or upload the module zip file and extract it
   ```

3. Update the addons list in Odoo and install the module:
   - Go to Apps > Update Apps List
   - Search for "Twilio SMS" and click Install

## Configuration

1. Go to Settings > General Settings
2. Find the "Twilio SMS Settings" section
3. Fill in the following fields:
   - **Account SID**: Your Twilio Account SID
   - **Auth Token**: Your Twilio Auth Token
   - **From Number**: Your Twilio phone number (with country code)
   - **Overwrite Odoo SMS**: Check this to use Twilio instead of Odoo's default SMS service

## Usage

Once configured, the module will automatically use Twilio for sending SMS messages when the "Overwrite Odoo SMS" option is enabled. You can send SMS through:

- Contact forms (SMS button)
- SMS Marketing campaigns
- Programmatic SMS sending via the `sms.sms` model

## Error Handling

If an SMS fails to send, the system will record the error message from Twilio in the SMS record. You can view these errors by:

1. Enabling developer mode
2. Going to Technical > SMS > SMS Messages
3. Checking the "Error Message" field on failed SMS records

## Troubleshooting

- **SMS not sending**: Verify your Twilio credentials and ensure your account has sufficient credits
- **Error messages**: Check the SMS record for specific error details from Twilio
- **Module not appearing**: Clear your browser cache and restart the Odoo server

## License

This module is licensed under LGPL-3.

## Authors

- Christopher Lynn South and Claude
- Website: https://001.com.mx

## Support

For questions or support, please contact:
- Email: chris@001.com.mx
- Website: https://001.com.mx

---

*Note: This module is not officially affiliated with Twilio Inc.*
