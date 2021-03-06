
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
    'name': 'BoM Field fixed',
    'summary': 'B0M',
    'version': '12.0',

    'description': """
This module creates a field named NAME in the Bill of Materials view form and tree view.
==============================================


    """,

    'author': 'Edwin de los santos',
    'maintainer': 'Edwin de los santos',
    'website': 'https://tidosgarcia.ddns.net/',

    'license': 'AGPL-3',
    'category': 'Manufacturing',

    'depends': [
        'base','mrp'
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
