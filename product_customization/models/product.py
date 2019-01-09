# -*- coding: utf-8 -*-

from odoo import models, fields, api
import odoo.addons.decimal_precision as dp


class ProductProduct(models.Model):
    _inherit = 'product.template'

    company_currency_id = fields.Many2one("res.currency", default=74)
    wh_cost = fields.Monetary(string='Costo de Almacenamiento', currency_field="company_currency_id")
    new_cost = fields.Monetary(string='Costo', currency_field="company_currency_id", default=lambda self: self.standard_price)

    @api.onchange('new_cost')
    def _onchange_df_cost(self):
        if self.new_cost > 0:
            self.standard_price = self.new_cost
        else:
            pass


    @api.multi
    def write(self,vals):
        try:
           if vals['new_cost'] > 0:
	      vals['standard_price'] = vals['new_cost']
	except Exception:
	   pass
	res = super(ProductProduct, self).write(vals)
        return res
    
    @api.model
    def update_df_cost(self):
	print "update cost trigger"
        recs = self.env['product.template'].search([])
	for rec in recs:
	    print "rec"
            rec.new_cost = rec.standard_price

    #Requerimiento especial, Dos garcia, cuando sea el producto servicio, que el costo sea lo mismo que el precio
    @api.depends('standard_price', 'list_price')
    @api.multi
    def _get_product_margin_porcent(self):
        for line in self:
            if line.list_price != 0 and line.standard_price:
                line.margin_porcent = (1-(line.standard_price / line.list_price)) * 100
            # elif self.standard_price == 0:
            #     line.margin_porcent = line.list_price
            else: 
                line.margin_porcent = 0.00

    @api.multi
    def view_wizard_modify_fields(self,view,name):
        res = {}
        
        for record in self:

            res = {
                    'name': '¿Desea cambiar el {} del producto ?'.format(name),
                    'type': 'ir.actions.act_window',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'modify_product.fields',
                    'view_id': view,
                    'target': 'new',
                    'flags': {'action_buttons': False},
                    'context': {'default_product_id': record.id,
                    'default_wh_cost': record.wh_cost,
                    'default_margin_porcent': record.margin_porcent,
                    'default_list_price': record.list_price,
                    'default_list_price_new': record.list_price}

                }
        return res

    @api.multi
    def action_set_whcost(self):
        modify_whcost_view= self.env['ir.model.data'].xmlid_to_res_id('product_customization.view_modify_product_field_wh_cost')

        return self.view_wizard_modify_fields(modify_whcost_view,'costo de almacen')

    @api.multi
    def action_set_list_price_by_margen(self):
        modify_margin_view= self.env['ir.model.data'].xmlid_to_res_id('product_customization.view_modify_product_field_margin_porcent')
        
        return self.view_wizard_modify_fields(modify_margin_view,'margen')




    margin_porcent = fields.Float(
        compute='_get_product_margin_porcent',
        string=u'Margen %',
        help="Muestra el porciento del margen",
    )

