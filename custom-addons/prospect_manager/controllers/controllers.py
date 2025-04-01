# -*- coding: utf-8 -*-
# from odoo import http


# class ProspectManager(http.Controller):
#     @http.route('/prospect_manager/prospect_manager', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prospect_manager/prospect_manager/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('prospect_manager.listing', {
#             'root': '/prospect_manager/prospect_manager',
#             'objects': http.request.env['prospect_manager.prospect_manager'].search([]),
#         })

#     @http.route('/prospect_manager/prospect_manager/objects/<model("prospect_manager.prospect_manager"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prospect_manager.object', {
#             'object': obj
#         })

