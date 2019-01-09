
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from openerp import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    cycle_sel=[
        ('intro','Introduccion'),
        ('grouth','Crecimiento'),        
        ('maturity','Madurez'),        
        ('decline','Declive'),        
        ('obsolet','Obsoleto'),        
    ]
    cycle = fields.Selection(cycle_sel,
        string=u'Ciclo de vida',
        default='maturity'
    )

    @api.multi
    def _count_claims(self):
        for rec in self:
            claims = self.env['claim.line'].search([('product_id.product_tmpl_id', '=', rec.id)])
            rec.claim_count = len(claims)

    
    claim_count = fields.Integer(compute="_count_claims", string="Reclamaciones")

    @api.multi
    def claim_action(self):
        action = self.env.ref("claim_product.crm_claim_action_stock")
        result = action.read()[0]
        
        claimslines = self.env['claim.line'].search([('product_id.product_tmpl_id','=',self.id)])
        ids=[]
        for line in claimslines:
            ids.append(line.claim_id.id)
        result['context'] = {'default_id': ids[0]}
        result['domain'] = "[('id', 'in', "+ str(ids) +")]"
        return result