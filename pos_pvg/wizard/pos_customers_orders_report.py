# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class posCustoemrsOrdersReport(models.TransientModel):
    _name = 'pos.customers.orders.report.wizard'
    _description = 'POS Customers Orders Report Wizard'

    start_date = fields.Datetime(required=True,)
    end_date = fields.Datetime(required=True,)

    customers = fields.Many2many('res.partner',)

    products = fields.Many2many('product.template',)

    @api.multi
    def generate_report(self):
        for record in self:
            if record.customers:
                for customer in record.customers:
                    self.env['pos.customer.orders.report'].create({'customer': customer.id, 'products': record.products.ids, 'start_date': record.start_date,'end_date': record.end_date})
            return {'type': 'ir.actions.act_window_close'}

