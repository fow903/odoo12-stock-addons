# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

class stockpicking(models.Model):
    _inherit='stock.picking'

    @api.model
    def _compute_total(self):
        for rec in self:
            packs = self.env['stock.move'].search([('picking_id', '=', rec.id)])
            li = []
            for pack in packs:
                li.append(pack.list_price*pack.quantity_done)
            rec.total_g=sum(li)

    total_g=fields.Float(string="TOTAL: ",compute='_compute_total')
