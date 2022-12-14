# -*- coding: utf-8 -*-
import datetime
import random
from odoo import models, fields, api

# add base class
class Base(models.Model):
    _name = 'rubrica.base'
    _description = 'Base class to be inherited'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         'El nombre debe ser único'),
    ]


# add a alumnos models
class Alumno(models.Model):
    _name = 'rubrica.alumno'
    _description = 'Alumnos de la prueba'

    nombre = fields.Char(string='Nombre', required=True)
    edad = fields.Integer(string='Edad')
    notasProgramacion = fields.Float(string='Nota Programación')
    notasDDI = fields.Float(string='Nota DDI')
    media = fields.Float(string='Media', compute='_compute_media')

    # add float media field de las notas
    @api.depends('notasProgramacion', 'notasDDI')
    def _compute_media(self):
        for record in self:
            record.media = (record.notasProgramacion + record.notasDDI) / 2


# clase hija de alumno
class Alumno2(models.Model):
    _name = 'rubrica.alumno2'
    _description = 'Alumnos de la prueba'
    _inherit = 'rubrica.alumno'

    nombre = fields.Char(string='Nombre', required=True)
    edad = fields.Integer(string='Edad')
    notasProgramacion = fields.Float(string='Nota Programación')
    notasDDI = fields.Float(string='Nota DDI')
    media = fields.Float(string='Media', compute='_compute_media')
    asignatura_id = fields.Many2one('rubrica.asignatura', string='Asignatura')

    # add float media field de las notas
    @api.depends('notasProgramacion', 'notasDDI')
    def _compute_media(self):
        for record in self:
            record.media = (record.notasProgramacion + record.notasDDI) / 2

# add a profesores models
class Profesor(models.Model):
    _name = 'rubrica.profesor'
    _description = 'Profesores de la prueba'

    nombre = fields.Char(string='Nombre', required=True)
    asignatura_id = fields.Many2one('rubrica.asignatura', string='Asignatura')

# add a asignaturas models
class Asignatura(models.Model):
    _name = 'rubrica.asignatura'
    _description = 'Asignaturas de la prueba'

    nombre = fields.Char(string='Nombre', required=True)
    profesor_id = fields.Many2one('rubrica.profesor', string='Profesor')
    alumno_id = fields.Many2many('rubrica.alumno', string='Alumnos')

# logo del modulo.
class Logo(models.Model):
    _name = 'rubrica.logo'
    _description = 'Logo de la prueba'

    name = fields.Char(string='Nombre', required=True)
    logo = fields.Binary(string='Logo', required=True)

