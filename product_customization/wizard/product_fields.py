# -*- coding: utf-8 -*-
from odoo import models, fields, api,exceptions
import odoo.addons.decimal_precision as dp

class ProductFields(models.Model):
    _name = 'modify_product.fields'


    @api.depends('product_id','margin_porcent')
    def _compute_list_price_new(self):
        for record in self:
            cost = record.product_id.standard_price
            marginp = record.margin_porcent
            if  cost != 0 and marginp > 0.00 and marginp < 100:
                record.list_price_new = cost / (1 - (marginp/ 100))
            elif cost ==0 and marginp > 0.00 and marginp < 100:
                raise exceptions.UserError("No se puede modificar el margen si el costo del producto es igual a 0!" )
            else:
                raise exceptions.UserError("El margen no puede ser ni menor que 0 ni mayor a 99 !" )


    product_id = fields.Many2one('product.template', string='Producto')
    company_currency_id = fields.Many2one("res.currency", default=74)
    wh_cost = fields.Monetary(string='Costo de Almacen',currency_field="company_currency_id")
    list_price = fields.Float('Precio de venta actual', digits_compute=dp.get_precision('Product Price'), help="Precio de  Venta del Producto Actual")
    list_price_new = fields.Float('Precio de venta modificado ', digits_compute=dp.get_precision('Product Price'),
     help="Valor por el cual va a ser modificado el precio de venta", compute='_compute_list_price_new')
    margin_porcent = fields.Float(
        string=u'Margen %',
        help="Muestra el porciento del margen"
    )    
   

    @api.multi
    def change_product_fields_wh_cost(self):
        print("====> Cambio el Costo del Almacen")
        self.product_id.write({'wh_cost': self.wh_cost})

    @api.multi
    def change_product_fields_list_price_by_margin(self):
        print("====> Cambio el Porciento del Margen")
        cost = self.product_id.standard_price
        marginp = self.margin_porcent

        if  cost != 0 and marginp > 0.00 and marginp < 100:
            self.product_id.write({'list_price': self.list_price_new})
        elif cost ==0 and marginp > 0.00 and marginp < 100:
            raise exceptions.UserError("No se puede modificar el margen si el costo del producto es igual a 0!" )
        else:
            raise exceptions.UserError("El margen no puede ser ni menor que 0 ni mayor a 99 !" )
        