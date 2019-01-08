
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from openerp import models, fields, api, _
from openerp.exceptions import UserError
from openerp import tools



class StockUpdate(models.Model):
    _name ='stock.update'
    _rec_name='inventory_id'
    pbarcode = fields.Char(string='Codigo de barras producto')


    @api.onchange('pbarcode')
    def get_product(self):
        for rec in self:
            product = self.env['product.product'].search([('barcode','=',rec.pbarcode)],limit=1)
            rec.product_name = product.name
            rec.product_id = product.id
            rec.product_uom_id = product.uom_id.id

    lbarcode = fields.Char(string='Codigo de barras Ubicacion')


    @api.onchange('lbarcode')
    def get_location(self):
        for rec in self:
            location= self.env['stock.location'].search([('barcode','=',rec.lbarcode)],limit=1)
            rec.location_id = location.id
            rec.location_name = location.name
        

    product_id = fields.Integer(string='Id producto')
    product_name = fields.Char(string='Producto',readonly=True)
    location_id = fields.Integer(string='Id location')  
    location_name = fields.Char(string='Ubicacion',readonly=True)
    state = fields.Selection(
        string='Estado',
        selection=[('draft', 'Borrador'), ('confirm', 'Iniciado'),('done', 'Terminado')],
        default='draft'
    )
    product_uom_id = fields.Integer(string='Unidad de medida')
    inventory_id = fields.Many2one('stock.inventory','Inventario')
    inventory_set = fields.Boolean(string=u'Inventory_set',default=False)
    
    @api.onchange('location_id','product_id')
    def get_amount(self):
        if self.product_id and self.inventory_id:
            for rec in self:
                inv_line = self.env['stock.inventory.line'].search([
                    ('location_id','=',rec.location_id),
                    ('product_id','=',rec.product_id),
                    ('inventory_id','=',rec.inventory_id.id)
                    ],limit=1)
                rec.new_quantity = inv_line.product_qty 
                
        else:
            pass

    new_quantity = fields.Float(string='Nueva cantidad a mano' )

    @api.multi
    def updatenum(self):
        l_exist = self.env['stock.inventory.line'].search([
                ('product_id','=',self.product_id),
                ('location_id','=',self.location_id),
                ('inventory_id','=',self.inventory_id.id)
                ])
            
        if l_exist:
            l_exist.write({
                          'product_id': self.product_id,
                          'product_qty': self.new_quantity,
                          'product_uom_id': self.product_uom_id,
                          'location_id':  self.location_id,
                          'inventory_id' : self.inventory_id.id
                          })
        else:
            self.env['stock.inventory.line'].create({
                          'product_id': self.product_id,
                          'product_qty': self.new_quantity,
                          'product_uom_id': self.product_uom_id,
                          'location_id':  self.location_id,
                          'inventory_id' : self.inventory_id.id
                          })
        if self.inventory_set==True:
            pass
        else:
            self.inventory_set = True
            self.state = 'confirm'
        self.pbarcode = ''
        self.lbarcode = ''
        self.new_quantity = ''
        return True


class DinamicUpdate(models.Model):
    _name = 'dinamic.update'
    _rec_name = 'ubicacion'
    pbarcode = fields.Char(string='Codigo de barras producto')


    @api.onchange('pbarcode')
    def get_product(self):
        for rec in self:
            product = self.env['product.product'].search([('barcode', '=', rec.pbarcode)], limit=1)
            rec.product_name = product.name
            rec.product_id = product.id
            rec.product_uom_id = product.uom_id.id

    lbarcode = fields.Char(string='Codigo de barras Ubicacion')

    @api.onchange('lbarcode')
    def get_location(self):
        for rec in self:
            location = self.env['stock.location'].search([('barcode', '=', rec.lbarcode)], limit=1)
            rec.location_id = location.id
            rec.location_name = location.name

    product_id = fields.Integer(string='Id producto')
    is_clear = fields.Boolean(string='Poner todo en 0',default=False)
    product_name = fields.Char(string='Producto')
    ubicacion = fields.Many2one(string='Almacen',comodel_name='stock.location')
    location_id = fields.Integer(string='Id location')
    location_name = fields.Char(string='Ubicacion')
    state = fields.Selection(
        string='Estado',
        selection=[('draft', 'Borrador'), ('confirm', 'Iniciado'), ('done', 'Terminado')],
        default='draft'
    )
    product_uom_id = fields.Integer(string='Unidad de medida')
    inventory_set = fields.Boolean(string=u'Inventory_set', default=False)

    @api.onchange('lbarcode', 'pbarcode')
    def get_amount(self):
        self.get_product()
        self.get_location()
        if not self.lbarcode or not self.pbarcode or not self.location_name or not self.product_name:
            for rec in self:
                rec.new_quantity = 0
                rec.product_id = ''
        elif self.product_id:
            for rec in self:
                product = self.env['product.product'].browse(self.product_id)
                available_qty = product.with_context({'location': self.location_id}).qty_available
                rec.new_quantity = available_qty
        else:
            print 'passing'
            pass

    new_quantity = fields.Float(string='Nueva cantidad a mano')

    @api.multi
    def set_to_zero(self):
        if self.location_id:
            inventory_obj = self.env['stock.inventory']
            name = 'set 0 inv loc {}'.format(self.location_id)
            inventory_id = inventory_obj.create({
                'name': _('INV: %s') % tools.ustr(name),
                'filter': 'none',
                'location_id': self.location_id})

            inventory_id.prepare_inventory()
            for rec in inventory_id.line_ids:
                if self.is_clear and self.product_id:
                    if rec.product_id.id == self.product_id:
                        pass
                    else:
                        rec.unlink()
                elif self.is_clear and not(self.product_id):
                    pass
                elif not self.is_clear and self.product_id:
                    if (rec.location_id.id == inventory_id.location_id.id) and (rec.product_id.id == self.product_id):
                        pass
                    else:
                        rec.unlink()

                else:
                    if rec.location_id == inventory_id.location_id:
                        pass
                    else:
                        rec.unlink()

            inventory_id.reset_real_qty()
            inventory_id.action_done()
            self.pbarcode = ''
            self.lbarcode = ''
            self.new_quantity = ''
            self.is_clear = False
        else:
            raise ValueError('Se debe especificar la localizacion y el producto para poder establecer la cantidad a 0')

    @api.multi
    def updatenum(self):
        inventory_obj = self.env['stock.inventory']
        inventory_line_obj = self.env['stock.inventory.line']

        inventory_id = inventory_obj.create({
            'name': _('INV: %s') % tools.ustr(self.ubicacion.name),
            'filter': 'none',
            'location_id': self.location_id})


        inventory_line_obj.create({
            'product_id': self.product_id,
            'product_qty': self.new_quantity,
            'product_uom_id': self.product_uom_id,
            'location_id': self.location_id,
            'theoretical_qty': self.new_quantity,
            'inventory_id': inventory_id.id
        })

        done = inventory_id.action_done()
        self.pbarcode = ''
        self.lbarcode = ''
        self.new_quantity = ''
        return True







