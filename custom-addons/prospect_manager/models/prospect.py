from email.policy import default

from odoo.api import readonly

from odoo import fields, models, api


class Prospect(models.Model):
    _name = 'prospect'
    _description = 'Prospects'

    name = fields.Char(required = True , size = 10)
    user_id = fields.Many2one('res.users', string='Assigned To', required = True , default = lambda self : self.env.user.id)
    status = fields.Selection([('contact_prospect', 'Contact prospect'), ('offer_sent', 'Offer sent'), ('won', 'Won') ,('lost','Lost')], string='Current Status', required=True
                              , default = 'contact_prospect' , readonly = True)
    customer_id = fields.Many2one('res.partner', string='Potential customer', required = True)
    lead_score = fields.Selection([(str(i), str(i)) for i in range(1, 6)], string='Probability of conversion', required=True)
    description = fields.Text(string='Description' , size = 30)
    phone = fields.Char(string='Phone' , size = 10)
    is_team_leader = fields.Boolean(string='Is Team Leader', compute='_check_team_leader')




    @api.depends('user_id')
    def _check_team_leader(self):
        """
                 Determines if the user is a team leader.
                 This method checks if the 'user_id' is associated with any CRM team.
                 If found, computational field 'is_team_leader' is set to True; otherwise, it's set to False
                 'is_team_leader' will be used to determine weather 'user_id' is going to be readonly or not.
                 """
        for rec in self:
            team = self.env['crm.team'].search([('user_id', '=', self.env.user.id)], limit=1)
            if team:
                rec.is_team_leader = True
            else:
                rec.is_team_leader = False



    @api.onchange('user_id')
    def _set_users_domain(self):


