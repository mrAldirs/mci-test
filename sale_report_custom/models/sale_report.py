from odoo import models, fields


class SaleReportCustom(models.Model):
    _name = 'sale.report.custom'
    _description = 'General Sale Report'
    _auto = False

    product_name = fields.Char(string='Product Name')
    product_internal_reference = fields.Char(string='Product Internal Reference')
    product_category = fields.Char(string='Product Category')
    sale_order_number = fields.Char(string='Sale Order Number')
    transfer_number = fields.Char(string='Transfer Number')
    invoice_number = fields.Char(string='Invoice Number')
    sale_type = fields.Char(string='Sale Type')
    quantity = fields.Float(string='Quantity')
    price = fields.Float(string='Price')
    discount = fields.Float(string='Discount')
    discount_amount = fields.Float(string='Discount Amount')
    price_subtotal = fields.Float(string='Price Subtotal')
    payment_terms = fields.Char(string='Payment Terms')
    payment_date = fields.Date(string='Payment Date')
    invoice_payment_status = fields.Char(string='Invoice Payment Status')

    def init(self):
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW sale_report_custom AS (
                SELECT
                    row_number() OVER () AS id,
                    pt.name as product_name,
                    pt.default_code as product_internal_reference,
                    pc.name as product_category,
                    so.name as sale_order_number,
                    sm.origin as transfer_number,
                    am.name as invoice_number,
                    so.state as sale_type,
                    sol.product_uom_qty as quantity,
                    sol.price_unit as price,
                    sol.discount as discount,
                    (sol.price_unit * sol.product_uom_qty * sol.discount / 100) as discount_amount,
                    sol.price_subtotal as price_subtotal,
                    ptm.name as payment_terms,
                    MAX(ap.payment_date) as payment_date,
                    am.invoice_payment_state as invoice_payment_status
                FROM
                    sale_order_line sol
                JOIN
                    sale_order so ON sol.order_id = so.id
                JOIN
                    product_product pp ON sol.product_id = pp.id
                JOIN
                    product_template pt ON pp.product_tmpl_id = pt.id
                JOIN
                    product_category pc ON pt.categ_id = pc.id
                LEFT JOIN
                    stock_move sm ON sm.origin = so.name
                LEFT JOIN
                    sale_order_line_invoice_rel solir ON sol.id = solir.order_line_id
                LEFT JOIN
                    account_move_line aml ON solir.invoice_line_id = aml.id
                LEFT JOIN
                    account_move am ON aml.move_id = am.id
                LEFT JOIN
                    account_invoice_payment_rel aipr ON am.id = aipr.invoice_id
                LEFT JOIN
                    account_payment ap ON aipr.payment_id = ap.id
                LEFT JOIN
                    account_payment_term ptm ON so.payment_term_id = ptm.id
                WHERE
                    am.state = 'posted'
                GROUP BY
                    pt.name, pt.default_code, pc.name, so.name, sm.origin, am.name, so.state, sol.product_uom_qty, sol.price_unit, sol.discount, sol.price_subtotal, ptm.name, am.invoice_payment_state
            )
        """)
