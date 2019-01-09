
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __odoo__.py file at the root folder of this module.                   #
###############################################################################

from odoo import models, fields
 
class ModelName(models.Model):
     _inherit = ['mrp.bom']
    
     nombre = fields.Char(
         string='Nombre BoM',
         required=False,
         readonly=False,
         index=True,
         default='[DGPR-    -LM-]',
         help=False,
         translate=True
     )
 

