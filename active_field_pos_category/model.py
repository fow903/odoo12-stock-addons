
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from openerp import models, fields, api

class PosCategory(models.Model):
    _inherit = 'pos.category'  
    active = fields.Boolean(
        string='Activo',
        default=True
    )
