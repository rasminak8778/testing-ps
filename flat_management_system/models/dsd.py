# -*- coding: utf-8 -*-
from odoo import fields, models


class FlatFlasdsat(models.Model):
    _name = 'adsad.flat'
    _description = 'Flats For Sale'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    name = fields.Char('namesssssssssssssaaaaaaaaaaaaaaaaaaaaaa', required=True)
    description = fields.Char(string='Description',
                              help='Description for the flat')
