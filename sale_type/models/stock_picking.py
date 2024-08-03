from odoo import fields, models, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sale_type_id = fields.Many2one('sale.type', string='Sale Type', compute='_compute_sale_type_id', store=True)

    @api.depends('origin')
    def _compute_sale_type_id(self):
        for record in self:
            sale_order = self.env['sale.order'].search([('name', '=', record.origin)], limit=1)
            record.sale_type_id = sale_order.sale_type_id.id