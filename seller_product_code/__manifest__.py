# -*- coding: utf-8 -*-
{
    'name': "Codigo Proveedor",
    'summary': 'Codigo del producto del vendedor',

    'description': """
        Cambios y Ajustes  en  inventario:
        mostrar en la vista lista el campo codigo del producto del proveedor
    """,

    'author': "Joel Payan",
    'category': 'Warehouse Management',
    'version': '0.1',
    'depends': ['base', 'product', 'stock'],

    'data': [
        'views/stock_view_tree.xml',
    ],

    "installable": True,

}
