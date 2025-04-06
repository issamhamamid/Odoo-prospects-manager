# -*- coding: utf-8 -*-
{
    'name': "prospect_manager",

    'summary': "Odoo prospects manager",

    'description': """
    technical test module to manage prospects
    """,

    'author': "Hammamid Ahmed Issam",
    'website': "",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base' , 'crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/region_view.xml',
        'views/team_view.xml',
        'views/prospect_view.xml',
        'views/client_view.xml',
        'views/base_menus.xml',
        'report/client_report.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

