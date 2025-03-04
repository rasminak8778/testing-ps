# -*- coding: utf-8 -*-
from odoo import fields, models


class FlatFlats(models.Model):
    _name = 'flat.flats'
    _description = 'Flats For Sale'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    name = fields.Char('namesssssssssssss', required=True)
    description = fields.Char(string='Description', help='Description for the flat')
    amount = fields.Float(string='Amount')
    flat_id = fields.Many2one('flat.management', string="Flat")
    
    sum= fields.Float(string='Sum')
    location = fields.Char(string='Location', help='Flat location')
    size = fields.Float(string='Size (sq ft)', help='Flat size in square feet')
    num_bedrooms = fields.Integer(string='Number of Bedrooms', help='Total bedrooms in the flat')
    num_bathrooms = fields.Integer(string='Number of Bathrooms', help='Total bathrooms in the flat')
