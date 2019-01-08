from openerp import fields, models


class stockquants(models.Model):
    _inherit = 'stock.quant'

    SELS = [('consu','Consmible'),
            ('product','Almacenable'),
            ('service','Servicio')]

    product_type = fields.Selection(SELS,string="Tipo de Producto",related="product_id.type",store=True)