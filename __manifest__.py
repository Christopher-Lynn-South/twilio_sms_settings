# -*- coding: utf-8 -*-

{
    "name": "Corp 001 Twilio SMS",
    "summary": "Send SMS using Twilio SMS Gateway, overwriting the default Odoo IAP SMS.",
    "description": """
    This plugin is used to overwrite the Odoo default SMS IAP with the Twilio SMS.
    
    To Configure:
        * Go to the Settings > General Settings. 
        * Search for Twilio Settings.
        * Add the Twilio Details like: Account SID, Auth Token, Number From.
        * Overwrite Odoo SMS if check then system will use Twilio SMS Settings, if not then Odoo SMS IAP. 
    """,
    "version": "18.0.1.0.0",
    "depends": [
        'sms',
    ],
    "category": "Tools",
    "website": "https://001.com.mx",
    "author": "Christopher Lynn South and Claude",
    "url": "https://001.com.mx",
    "license": "LGPL-3",
    "data": [
        'views/configuration.xml',
        'views/sms_sms.xml',
    ],
    'external_dependencies': {"python": ['twilio']},
    "application": False,
    "installable": True,
    "auto_install": False,
}