# -*- coding: utf-8 -*-
{
    'name': 'Sale Report Custom',
    'version': '13.0.1.0.0',
    'summary': 'Custom Sale Report Module',
    'author': 'Aldi',
    'website': 'https://www.aldi.com',
    'category': 'Sales',
    'depends': ['sale_management', 'account', 'sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_report_views.xml',
    ],
    'installable': True,
    'application': False,
}
