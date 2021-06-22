from odoo import models,fields

class RealEsateWizard(models.TransientModel):
   _name = 'real.estate.wizard'
   _description = 'Real estate Wizard'

   sale_order = fields.Many2one('sale.order',string='Sale order')