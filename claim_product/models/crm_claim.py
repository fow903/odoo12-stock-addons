
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from openerp import models, fields, api, _
from openerp.exceptions import UserError, ValidationError


class CrmClaim(models.Model):
    _inherit = 'crm.claim'
    selections = [
        ('sale_order','Cotizacion/Pedido'),
        ('employee','Empleado'),
        ('invoice','Factura'),
        ('purchase_order','Cotizacion/Orden de compra'),
        ('delivery_slip','Conduce'),
        ('product','Producto'),        
    ]
    referencia = fields.Selection(selections,string='Referencia')
    sale_order = fields.Many2one('sale.order',string='Cotizacion/Pedido')
    employee = fields.Many2one('hr.employee',string='Empleado')
    invoice = fields.Many2one('account.invoice',string='Factura')
    purchase = fields.Many2one('purchase.order',string='Orden de Compra')
    delivery_slip = fields.Many2one('stock.picking',string='Conduce')
    # product = fields.Many2one('product.template',string='Producto')
    partner = fields.Many2one('res.partner',string='Contacto')
    claim_lines = fields.One2many('claim.line','claim_id',string='Lineas de productos')
class ClaimLine(models.Model):
    _name = 'claim.line'
    _description = 'Claim Line'
    _order = 'claim_id desc, id'
    @api.model
    def create(self, values):
        onchange_fields = ['name']
        if values.get('claim_id') and values.get('product_id') and any(f not in values for f in onchange_fields):
            line = self.new(values)
            line.product_id_change()
            for field in onchange_fields:
                if field not in values:
                    values[field] = line._fields[field].convert_to_write(line[field])
        else:
            print 'No existe la reclamacion'
        try:
            line = super(ClaimLine, self).create(values)
            return line
        except Exception as e:
            print 'Error {}'.format(e)
        return None

    def get_domain(self):
        products = []
        if self.claim_id.referencia=='sale_order':
            if self.claim_id.sale_order:
                so = self.env['sale.order'].search([('id','=',self.claim_id.sale_order.id)])
                for line in so.order_line:
                    products.append(line.product_id.id)
                print products
                return products
        elif self.claim_id.referencia=='invoice':
            if self.claim_id.invoice:
                inv = self.env['account.invoice'].search([('id','=',self.claim_id.invoice.id)])
                for line in inv.invoice_line_ids:
                    products.append(line.product_id.id)
                print products
                return products
        elif self.claim_id.referencia=='delivery_slip':
            if self.claim_id.delivery_slip:
                delivery = self.env['stock.picking'].search([('id','=',self.claim_id.delivery_slip.id)])
                for line in delivery.pack_operation_product_ids:
                    products.append(line.product_id.id)
                for line in delivery.move_lines:
                    products.append(line.product_id.id)
                print products
                return products
        else:
            return products
    
    @api.onchange('product_id')
    def _onchange_product_id(self):
        res = {}
        if self.claim_id.referencia:
            res['domain'] = {'product_id': [('id', 'in', self.get_domain() )]}
        else:
            res['domain'] = {'product_id': []}
        print res
        return res
    
    name = fields.Text(string=u'Descripción', required=True)
    claim_id = fields.Many2one('crm.claim',string='Order Reference', ondelete='cascade', index=True, copy=False) 
    product_id = fields.Many2one('product.product','Producto' , ondelete='restrict', required=True)
    qty_line = fields.Integer('Cantidad')
    uom = fields.Many2one(string=u'Unidad de medida',comodel_name='product.uom')
    
    
    
