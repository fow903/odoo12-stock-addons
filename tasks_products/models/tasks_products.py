
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from openerp import models, fields, api, _

class ProductTasks(models.Model):
    _name = 'task.product'
    _rec_name  = 'nombre'
    nombre = fields.Char('Tarea')

