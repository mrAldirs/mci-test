from odoo import fields, models, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    # sale_line_ids = fields.Many2many(
    #     'sale.order.line',
    #     'sale_order_line_invoice_rel',
    #     'invoice_line_id', 'order_line_id',
    #     string='Sales Order Lines', readonly=True, copy=False, store=True)
