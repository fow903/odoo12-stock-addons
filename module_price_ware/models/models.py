# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging

class stockpicking(models.Model):
    _inherit='stock.picking'

    @api.model
    def _compute_total(self):
        for rec in self:
            packs = self.env['stock.pack.operation'].search([('picking_id', '=', rec.id)])
            li = []
            for pack in packs:
                print pack
                li.append(pack.list_price*pack.qty_done)
            rec.total_g=sum(li)
    total_g=fields.Float(string="TOTAL: ",compute='_compute_total')
