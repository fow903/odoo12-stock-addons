
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __openerp__.py file at the root folder of this module.                   #
###############################################################################

from openerp import models, fields
 
class ModelName(models.Model):
     _inherit = ['stock.picking']
    
     user_id = fields.Many2one('res.users','Preparado por :')
     vendedor = fields.Char('Vendedor',related='partner_id.user_id.name',readonly='True')
     
 

