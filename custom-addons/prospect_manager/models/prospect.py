from email.policy import default


from odoo import fields, models, api


class Prospect(models.Model):
    _name = 'prospect'
    _description = 'Prospects'

    name = fields.Char(required = True , size = 10)
    user_id = fields.Many2one('res.users', string='Assigned To', required = True)
    status = fields.Selection([('contact_prospect', 'Contact prospect'), ('offer_sent', 'Offer sent'), ('won', 'Won') ,('lost','Lost')], string='Current Status', required=True
                              , default = 'contact_prospect' , readonly = True)
    customer_id = fields.Many2one('res.partner', string='Potential customer', required = True)
    lead_score = fields.Selection([(str(i), str(i)) for i in range(1, 6)], string='Probability of conversion', required=True)
    description = fields.Text(string='Description' , size = 30)
    phone = fields.Integer(string='Phone' , size = 10)