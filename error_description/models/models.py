# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import UserError
class sale_order(models.Model):
    _inherit = 'sale.order.line'
   
    @api.onchange('product_id')
    def onchange_product_id(self):
        if not self.order_id.partner_id:
            raise UserError(("¡Atencion, Primero debe seleccionar el contacto!!"))

            
    
        