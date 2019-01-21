import datetime
import logging
_logger = logging.getLogger(__name__)
from odoo.osv import fields, osv

class stock_history(osv.osv):
    _inherit = 'stock.history'
    
    def read_group(self, cr, uid, domain, fields, groupby, offset=0, limit=None, context=None, orderby=False, lazy=True):
        res = super(stock_history, self).read_group(cr, uid, domain, fields, groupby, offset, limit=limit, context=context, orderby=orderby, lazy=lazy)
        if context is None:
            context = {}
        date = context.get('history_date', datetime.datetime.now())
        if 'net_value' in fields:
            group_lines = {}
            for line in res:
                domain = line.get('__domain', domain)
                group_lines.setdefault(str(domain), self.search(cr, uid, domain, context=context))
            line_ids = set()
            for ids in group_lines.values():
                for product_id in ids:
                    line_ids.add(product_id)
            lines_rec = {}
            if line_ids:
                move_ids = tuple(abs(line_id) for line_id in line_ids)
                cr.execute(
                    'SELECT id, product_id, price_unit_on_quant, company_id, quantity FROM stock_history WHERE move_id IN %s',
                    (move_ids,))
                lines_rec = tuple(rec for rec in cr.dictfetchall() if rec['id'] in line_ids)
            lines_dict = dict((line['id'], line) for line in lines_rec)
            product_ids = list(set(line_rec['product_id'] for line_rec in lines_rec))
            products_rec = self.pool['product.product'].read(cr, uid, product_ids, ['cost_method', 'id'],
                                                             context=context)
            products_dict = dict((product['id'], product) for product in products_rec)
            cost_method_product_ids = list(
                set(product['id'] for product in products_rec if product['cost_method'] != 'real'))
            histories = []
            if cost_method_product_ids:
                cr.execute(
                    'SELECT DISTINCT ON (product_id, company_id) product_id, company_id, cost FROM product_price_history WHERE product_id in %s AND datetime <= %s ORDER BY product_id, company_id, datetime DESC',
                    (tuple(cost_method_product_ids), date))
                histories = cr.dictfetchall()
            histories_dict = {}
            for history in histories:
                histories_dict[(history['product_id'], history['company_id'])] = history['cost']
            for line in res:
                value = 0.0
                lines = group_lines.get(str(line.get('__domain', domain)))
                for line_id in lines:
                    line_rec = lines_dict[line_id]
                    product = products_dict[line_rec['product_id']]
                    if product['cost_method'] == 'real':
                        price = line_rec['price_unit_on_quant']
                    else:
                        price = histories_dict.get((product['id'], line_rec['company_id']), 0.0)
                    value += price * line_rec['quantity']
                line['net_value'] = value
        return res

    def _compute_value(self, cr, uid, ids, name, attr, context=None):
        if context is None:
            context = {}

        date = str(datetime.datetime.now())
        price_history_obj = self.pool.get('product.price.history')
        product_obj = self.pool.get("product.product")
        res = {}
        last_price = self.browse(cr, uid, ids, context=context)[-1]
        for line in self.browse(cr, uid, ids, context=context):
            history_ids = price_history_obj.search(cr, uid, [('company_id', '=', line.company_id.id), ('product_id', '=', line.product_id.id), ('datetime', '<=', date)], limit=1)        
            if line.product_id.cost_method == 'real':
                # res[line.id] = last_price.price_unit_on_quant
                res[line.id] = line.quantity * line.product_id.product_tmpl_id.new_cost
            else:
                res[line.id] = line.quantity * line.product_id.product_tmpl_id.new_cost
                # res[line.id] = price_history_obj.read(cr, uid, history_ids[0], ['cost'], context=context)['cost'] if history_ids else 0.0

        return res


    def _compute_inventory_value(self, cr, uid, ids, name, attr, context=None):
        _logger.warning('Getting inventory Value')
        
        if context is None:
            context = {}
        date = context.get('history_date')
        product_obj = self.pool.get("product.product")
        res = {}
        last_price = self.browse(cr, uid, ids, context=context)[-1]
        for line in self.browse(cr, uid, ids, context=context):
            if line.product_id.cost_method == 'real':
                res[line.id] = line.quantity * line.product_id.product_tmpl_id.new_cost
            else:
                # res[line.id] = line.quantity * product_obj.get_history_price(cr, uid, line.product_id.id, line.company_id.id, date=date, context=context)
                res[line.id] = line.quantity * line.product_id.product_tmpl_id.new_cost

        return res


    _columns = {
        'single_value': fields.function(_compute_value, string="Costo de almacen", type='float', readonly=True),
        'net_value': fields.function(_compute_inventory_value, string="Valor de inventario", type='float', readonly=True),
    }
    