from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_type_id = fields.Many2one('sale.type', string='Sale Type')
