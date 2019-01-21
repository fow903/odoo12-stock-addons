import datetime

from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit ='product.template'

    @api.multi
    def compute_wh_cost(self):
        product_id = None
        try:
            product_id = self.env['product.product'].search([('product_tmpl_id','=',self.id)],limit=1)
        except ValueError as e:
            print('Error en producto')
        if product_id:
            if product_id.cost_method == 'real':
                history = self.env['stock.history'].search([('product_id','=',product_id.id)])
                if history:
                    self.wh_cost = history[-1].price_unit_on_quant
                else:
                    pass
            else:
                ph = self.env['product.price.history'].search([('product_id','=',product_id.id)])
                if ph:
                    self.wh_cost = ph[-1].cost
                else:
                    pass


   


    company_currency_id = fields.Many2one("res.currency", default=74)
    wh_cost = fields.Monetary(string='Costo de Almacen', currency_field="company_currency_id")