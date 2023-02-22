# -*- coding: utf-8 -*- 
from odoo import models, fields, api

class clases(models.Model):
    _name = 'clases.clases'
    _description = 'reserva de clases'

    name = fields.Char(string='Nombre')
    dni = fields.Char(string="DNI")
    fechainit = fields.Datetime(string='Dia y hora de inicio')
    # fechafin = fields.Datetime(string='Hora fin')
    tiempo = fields.Integer(string='Horas de clase')
    precio = fields.Float(string='Precio por hora')
    comentario = fields.Char(string='Comentario')
    total = fields.Float(compute='_value_price', store=True)
    
    @api.depends('precio', 'tiempo')
    def _value_price(self):
        for record in self:
            record.total = float(record.precio) * (record.tiempo)

class material(models.Model):
    _name= 'clases.material'
    _description= 'reserva del material'

    name = fields.Char(string='Nombre')
    dni = fields.Char(string="DNI")
    material = fields.Char(string="Material (nº referencia)")
    precio = fields.Float(string='Precio por hora')
    tiempo = fields.Integer(string='Horas de alquiler')
    fianza = fields.Float(string='Fianza')
    comentario = fields.Char(string='Comentario')
    total = fields.Float(compute='_value_material', store=True)

    @api.depends('precio', 'fianza', 'tiempo', 'total')
    def _value_material(self):
        for record in self:
            record.total = float(record.precio * record.tiempo) + (record.fianza)
