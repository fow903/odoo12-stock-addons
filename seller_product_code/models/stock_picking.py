# -*- coding: utf-8 -*-
from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    state_conduce_sel = [
        ('pending', 'Pendiente'),
        ('overdue', 'Vencido'),
        ('invoiced', 'Facturado'),
        ('refund', 'Devuelto'),
        ('partial', 'Devolución Parcial'),
    ]
    state_conduce = fields.Selection(state_conduce_sel, string=u'Estado', default=False)
