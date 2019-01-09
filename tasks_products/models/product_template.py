
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    tipo = fields.Selection([
        ('finished', 'Producto Terminado'),
        ('matter', 'Materia Prima')], string=u'Clasificación',
        help="Tipo de producto segun estado")

    tarea = fields.Many2one('task.product',
                            u'Estado de Mejora o Cambio')

