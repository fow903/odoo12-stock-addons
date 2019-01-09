# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def _compute_seller_pcode(self):
        for rec in self:
            if len(rec.seller_ids) > 0:
                rec.product_code_tree = rec.seller_ids[0].product_code

    product_code_tree = fields.Char(compute='_compute_seller_pcode')


