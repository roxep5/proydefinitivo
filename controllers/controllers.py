# -*- coding: utf-8 -*-
# from odoo import http


# class Proydefinitivo(http.Controller):
#     @http.route('/proydefinitivo/proydefinitivo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proydefinitivo/proydefinitivo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proydefinitivo.listing', {
#             'root': '/proydefinitivo/proydefinitivo',
#             'objects': http.request.env['proydefinitivo.proydefinitivo'].search([]),
#         })

#     @http.route('/proydefinitivo/proydefinitivo/objects/<model("proydefinitivo.proydefinitivo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proydefinitivo.object', {
#             'object': obj
#         })
