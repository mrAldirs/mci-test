from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_amount = fields.Float(string='Discount Amount')

    @api.onchange('discount_amount')
    def _onchange_discount_amount(self):
        for line in self:
            if line.discount_amount:
                line.discount = (line.discount_amount / (line.price_unit * line.product_uom_qty)) * 100
                line._compute_amount()

    def _prepare_invoice_line(self):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res['discount_amount'] = self.discount_amount
        return res