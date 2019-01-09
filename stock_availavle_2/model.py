
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields , api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    @api.onchange('product_id')
    @api.multi
    def compute_qty(self):
        for rec in self:
            if rec.product_id:
                product=self.env['product.product'].search([('id','=',rec.product_id.id)])
                rec.qty_available = product.qty_available
                print '=======>>>>>',product
    qty_available = fields.Integer(string=u'Disponible',compute = 'compute_qty')

   