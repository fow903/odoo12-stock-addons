# -*- coding: utf-8 -*-
{
    'name': "Customizacion de Los Productos",

    'summary': """
        Agregar Algunas mejoras al Productos""",

    'description': """
        Modificaciones al Producto
    """,

    'author': "Jorge Miguel Hernandez Santos",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Producto',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','warehouse_cost_v1'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'wizard/product_fields_views.xml'
    ],

}