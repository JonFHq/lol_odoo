# -*- coding: utf-8 -*-

from odoo import models, fields, api

class viaje(models.Model):
    _name = 'examen.viaje'
    _description = 'viaje'

    vehiculo = fields.Many2one("examen.vehiculo", string="Vehiculo", required=True)
    provincia_origen = fields.Reference(selection=[('examen.provincia', 'Provincia')], string="Provincia de origen", required=True)
    provincia_destino = fields.Reference(selection=[('examen.provincia', 'Provincia')], string="Provincia de destino", required=True)
    fecha = fields.Date(string="Fecha", required=True)