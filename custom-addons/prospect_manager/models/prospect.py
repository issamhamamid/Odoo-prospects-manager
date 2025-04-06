from odoo.api import readonly

from odoo import fields, models, api
from odoo.exceptions import UserError

class Prospect(models.Model):
    _name = 'prospect'
    _description = 'Prospects'

    name = fields.Char(required = True , size = 10)
    user_id = fields.Many2one('res.users', string='Assigned To', required = True , default = lambda self : self.env.user.id)
    status = fields.Selection([('contact_prospect', 'Contact prospect'), ('offer_sent', 'Offer sent'), ('won', 'Won') ,('lost','Lost')], string='Current Status', required=True
                              , default = 'contact_prospect' , readonly = True)
    lead_score = fields.Selection([(str(i), str(i)) for i in range(1, 6)], string='Probability of conversion', required=True)
    description = fields.Text(string='Description' , size = 30)
    phone = fields.Char(string='Phone' , size = 10 , required= True)
    is_team_leader = fields.Boolean(string='Is Team Leader', compute='_check_team_leader')
    user_id_domain = fields.Binary(string='User ID Domain', compute='compute_user_id_domain')
    offer_sent_date = fields.Date(string='Offer Sent Date', readonly=True)
    offer_won_date = fields.Date(string='Offer Won Date', readonly=True)
    offer_lost_date = fields.Date(string='Offer Lost Date', readonly=True)
    client_id = fields.Many2one('res.partner', string='Converted client', readonly=True)
    email = fields.Char(string='Email', size=50, required=True)



    @api.constrains('user_id')
    def _check_if_member(self):
        """
            This method checks if the user_id is a member of the CRM team.
            If not, it raises a UserError.
            """
        for prospect in self:
            team = self.env['crm.team'].search([('user_id', '=', self.env.user.id)], limit=1) or self.env['crm.team'].search([('member_ids', 'in', [self.env.user.id])], limit=1)
            if not team:
                raise UserError("You are not a member of any Commercial team.")

    @api.depends('user_id')
    def _check_team_leader(self):

        """
                 Determines if the user is a team leader.
                 This method checks if the 'user_id' is associated with any CRM team.
                 If found, computational field 'is_team_leader' is set to True; otherwise, it's set to False
                 'is_team_leader' will be used to determine weather 'user_id' is going to be readonly or not.
                 """
        for prospect in self:
            team = self.env['crm.team'].search([('user_id', '=', self.env.user.id)], limit=1)
            if team:
                prospect.is_team_leader = True
            else:
                prospect.is_team_leader = False




    @api.depends('user_id')
    def compute_user_id_domain(self):
        """
            Compute method to determine the domain for the user_id field.
            This method depends on the 'user_id' field. It searches for a CRM team
            where the current user is the leader. If a team is found, it sets the
           'user_id_domain' field to a domain that includes the IDs of the team members.
           If no team is found, the 'user_id_domain' remains untouched .
                            """
        for prospect in self:
            team = self.env['crm.team'].search([('user_id', '=', self.env.user.id)], limit=1)
            if team :
                members = team.member_ids.ids
                prospect.user_id_domain = [('id', 'in', members)]
            else:
                prospect.user_id_domain = []


    def action_offer_sent(self):
        """
            This method is triggered when the 'Offer Sent' button is clicked.
            It updates the status of the prospect to 'offer_sent'.
            """
        for prospect in self:
            if prospect.status == 'won':
                raise UserError("This prospect has been marked as Won.")
            if prospect.status == 'lost':
                raise UserError("This prospect has been marked as Lost.")
            prospect.offer_sent_date = fields.Date.today()
            prospect.status = 'offer_sent'



    def action_won(self):
        for prospect in self:
            if prospect.status == 'won':
                raise UserError("This prospect has already been marked as Won.")
            if prospect.status == 'lost':
                raise UserError("This prospect has been marked as Lost.")
            prospect.status = 'won'
            prospect.offer_won_date = fields.Date.today()
            partner = self.env['res.partner'].create([{
                'name': prospect.name,
                'email': prospect.email,
                'prospect_id': prospect.id,
                'phone': prospect.phone,
            }])
            prospect.client_id = partner.id



    def action_lost(self):
        for prospect in self:
            if prospect.status == 'won':
                raise UserError("This prospect been marked as Won.")
            if prospect.status == 'lost':
                raise UserError("This prospect has already been marked as Lost.")
            prospect.status= 'lost'
            prospect.offer_lost_date = fields.Date.today()
