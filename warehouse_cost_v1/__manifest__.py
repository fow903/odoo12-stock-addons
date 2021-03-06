
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
    'name': 'warehouse costs',
    'summary': 'warehouse costs Module Project',
    'version': '1.0',

    'description': """
warehouse costs Module Project.
==============================================


    """,

    'author': 'TM_FULLNAME',
    'maintainer': 'TM_FULLNAME',
    'contributors': ['TM_FULLNAME <TM_FULLNAME@gmail.com>'],

    'website': 'http://www.gitlab.com/TM_FULLNAME',

    'license': 'AGPL-3',
    'category': 'Uncategorized',

    'depends': [
        'base','stock_landed_costs','product'
    ],
    'external_dependencies': {
        'python': [
        ],
    },
    'data': [
                # 'wizard/stock_valuation_history.xml',
                'views/product_template.xml'

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
