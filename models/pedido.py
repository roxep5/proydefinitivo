
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pedido(models.Model):
     _name = 'proydefinitivo.pedido' # Será o nome da táboa
     _description = ' modelo pedidos'

     name = fields.Char(string="Identificador",required=True,size=20)
     # Os campos One2many Non se almacenan na BD
     lineapedido_ids = fields.One2many("proydefinitivo.lineapedido", 'pedido_id')

     def actualizadorSexo(self):
          informacion_ids = self.env['proydefinitivo.definitivo'].search([('autorizado', '=', False)])
          for rexistro in informacion_ids:
               self.env['proydefinitivo.definitivo']._cambia_campo_sexo(rexistro)