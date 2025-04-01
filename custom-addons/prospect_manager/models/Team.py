from odoo import fields, models, api


class Team(models.Model):
    _inherit = 'crm.team'
    _description = 'Commercial team'

    region_id = fields.Many2one('prospect.region', string='Region', required=True)
