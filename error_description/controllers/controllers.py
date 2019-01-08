# -*- coding: utf-8 -*-
from openerp import http

# class /odoo/modules/9.0/custom/addons/errorDescription(http.Controller):
#     @http.route('//odoo/modules/9.0/custom/addons/error_description//odoo/modules/9.0/custom/addons/error_description/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//odoo/modules/9.0/custom/addons/error_description//odoo/modules/9.0/custom/addons/error_description/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/odoo/modules/9.0/custom/addons/error_description.listing', {
#             'root': '//odoo/modules/9.0/custom/addons/error_description//odoo/modules/9.0/custom/addons/error_description',
#             'objects': http.request.env['/odoo/modules/9.0/custom/addons/error_description./odoo/modules/9.0/custom/addons/error_description'].search([]),
#         })

#     @http.route('//odoo/modules/9.0/custom/addons/error_description//odoo/modules/9.0/custom/addons/error_description/objects/<model("/odoo/modules/9.0/custom/addons/error_description./odoo/modules/9.0/custom/addons/error_description"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/odoo/modules/9.0/custom/addons/error_description.object', {
#             'object': obj
#         })