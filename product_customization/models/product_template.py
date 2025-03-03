# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    case_per_pallet = fields.Char(string="Cases Per Pallet", help="This is the cases per pallet")
