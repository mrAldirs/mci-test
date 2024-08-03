# -*- coding: utf-8 -*-
{
    'name': "Sale Type",
    'summary': "Custom module to add sale type to sale order and stock picking",
    'description': "",
    'author': "Aldi",
    'website': "http://www.aldi.com",
    'category': 'Sales',
    'version': '0.1',
    'depends': ['base', 'sale', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_type_views.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
}
