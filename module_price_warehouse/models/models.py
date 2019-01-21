# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'
    list_price = fields.Float('Precio Unitario',related='product_id.list_price')
    @api.depends('list_price','quantity_done')
    def _compute_total(self):

        for line in self:
            total = line.list_price * (line.quantity_done)

            line.update({
                'total_amount': total
            })

    total_amount = fields.Float(string='Precio total de cantidad realizada', compute='_compute_total')


