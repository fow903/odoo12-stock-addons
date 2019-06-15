from odoo import fields, api, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    shop_id = fields.Many2one('shop.config',"Sucursal")