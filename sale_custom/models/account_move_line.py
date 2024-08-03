from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    discount_amount = fields.Float(string='Discount Amount')

    @api.onchange('discount_amount')
    def _onchange_discount_amount(self):
        for line in self:
            if line.discount_amount:
                line.discount = (line.discount_amount / (line.price_unit * line.quantity)) * 100
                line._compute_amount()
