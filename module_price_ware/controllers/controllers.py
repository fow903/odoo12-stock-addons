# -*- coding: utf-8 -*-
from openerp import http

# class /odoo/modules/9.0/custom/addons/warehousePrice(http.Controller):
#     @http.route('//odoo/modules/9.0/custom/addons/warehouse_price//odoo/modules/9.0/custom/addons/warehouse_price/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//odoo/modules/9.0/custom/addons/warehouse_price//odoo/modules/9.0/custom/addons/warehouse_price/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/odoo/modules/9.0/custom/addons/warehouse_price.listing', {
#             'root': '//odoo/modules/9.0/custom/addons/warehouse_price//odoo/modules/9.0/custom/addons/warehouse_price',
#             'objects': http.request.env['/odoo/modules/9.0/custom/addons/warehouse_price./odoo/modules/9.0/custom/addons/warehouse_price'].search([]),
#         })

#     @http.route('//odoo/modules/9.0/custom/addons/warehouse_price//odoo/modules/9.0/custom/addons/warehouse_price/objects/<model("/odoo/modules/9.0/custom/addons/warehouse_price./odoo/modules/9.0/custom/addons/warehouse_price"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/odoo/modules/9.0/custom/addons/warehouse_price.object', {
#             'object': obj
#         })