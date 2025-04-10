{
    'name': "POS Cheque Payment Information",
    'summary': "Add Cheque as a Payment Method in Odoo POS – Compatible with Community & Enterprise",
    'description': """
POS Cheque Payment Method
==========================
This module allows businesses to accept cheque payments directly from the Point of Sale (POS) interface in Odoo. It provides a smooth and integrated way to register payments by cheque, enhancing flexibility and catering to customer needs.

Key Features:
-------------
- Add "Cheque" as a custom payment method in POS
- Seamless integration with Odoo’s POS session
- Works with both Odoo Community and Enterprise editions
- Easy to configure and use
- Suitable for retail, hospitality, and service-based businesses

Compatibility:
--------------
✅ Odoo Enterprise
✅ Odoo Community  


Support:
--------
For support, contact us at: contact@layamedconsulting.com
    """,
    'author': 'LAYAMED CONSULTING',
    'version': '17.0.1.0.0',
    'category': 'Point of Sale',
    'version': '1.0',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_payment_details.xml',
        'views/pos_payment_view.xml',
    ],

    'assets': {
        'point_of_sale._assets_pos': [
            'POS_Cheque_Payment_Method/static/src/app/**/*',
        ],
    },

    'images': ['static/description/banner.png'],
    'license': 'OPL-1',
    'price': 15.00,
    'currency': 'USD',
    'installable': True,
    'application': True,
    'auto_install': False,
}
