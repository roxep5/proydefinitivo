# -*- coding: utf-8 -*-

from odoo import models, fields, api


class proydefinitivo(models.Model):
    _name = 'proydefinitivo.definitivo'
    _description = 'Proyecto definitivo'

    autorizado = fields.Boolean(string="¿Autorizado?", default=True)
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
