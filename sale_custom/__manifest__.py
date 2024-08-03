{
    'name': 'Sale Custom',
    'version': '13.0.1.0.0',
    'summary': 'Custom module to add discount amount to sale order lines and invoice lines',
    'author': 'Aldi',
    'website': 'http://www.aldi.com',
    'category': 'Sales',
    'depends': ['sale', 'account'],
    'data': [
        'views/sale_order_line_views.xml',
        'views/account_move_line_views.xml',
    ],
    'installable': True,
    'application': False,
}
