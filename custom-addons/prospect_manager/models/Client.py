from odoo import fields, models, api


class Client(models.Model):
    _inherit = 'res.partner'
    _description = 'Client'

    prospect_id = fields.Many2one('prospect', string='Prospect', readonly=True)




    @api.onchange('phone')
    def _onchange_prospect_id(self):
       print('test')
       print(self.prospect_id.user_id.sale_team_id.id)