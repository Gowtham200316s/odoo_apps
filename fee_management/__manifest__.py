{
    'name': 'Fee management',
    'author': 'Gowtham A ',
    'category': 'Fee',
    'version': '15.0',
    'price': '10.0',
    'currency': 'USD',
    
    'summary': 'odoo 16 development',
    'description': """
This module information about fees""",
    'data': [

        'security/ir.model.access.csv',

        'wizard/lost.xml',

        'views/fee.xml',
        'views/lost_reason.xml',

        'views/menu.xml',

    ],
'depends': [
    'base', 'product'],

    'license': 'LGPL-3',
}
