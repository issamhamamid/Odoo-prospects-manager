from odoo import fields, models, api


class Region(models.Model):
    _name = 'prospect.region'
    _description = 'regions'

    name = fields.Char(required = True)
    commercial_lead_id = fields.Many2one('res.users', string='Commercial Lead' , required = True)
