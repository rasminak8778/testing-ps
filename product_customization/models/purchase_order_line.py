from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_uom = fields.Many2one(
        'uom.uom',
        string="UoM",
        domain="[('category_id', '=', product_uom_category_id),('uom_type', 'in', ['bigger', 'smaller'])]"
    )
