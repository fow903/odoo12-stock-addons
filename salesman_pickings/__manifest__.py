
# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#
#    Copyright (c) All rights reserved:
#        (c) 2015  TM_FULLNAME
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#
###############################################################################
{
    'name': 'Vendedor Conduce Salida',
    'summary': 'Conduce de Salida',
    'version': '1.0',

    'description': """
Este modulo le podra el campo vendedor a los conduce de salida
==============================================


    """,

    'author': 'Edwin de los santos',
    'maintainer': 'Edwin de los santos',
    'website': 'https://lacasadelled.com.do',

    'license': 'AGPL-3',
    'category': 'Manufacturing',

    'depends': [
        'base','stock'
    ],
    'external_dependencies': {
        'python': [
        ],
    },
    'data': ['views/view.xml'
    ],
    'demo': [
    ],
    'js': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'images': [
    ],
    'test': [
    ],

    'installable': True
}
