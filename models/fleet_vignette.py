# -*- coding: utf-8 -*-
from odoo import fields, models, api


class FleetList(models.Model):
    _name = 'egov_ma.hr.vignette'

    num_vingette = fields.Char('N° Vignette')
    amount = fields.Float('Montant')
    creat_date = fields.Datetime('Date de création')
    image = fields.Binary(attachment=True,
              help="This field holds the image used as vignette.")
    state = fields.Selection([
    ('available', 'Disponible'),
    ('affeted', 'Affecté'),
    ('used', 'Utilisé'),
    ], setting='Etat', readonly=True, default='available')


class Egovmacarnetsvignettes(models.Model):
    _name = 'egov_ma.carnets.vignettes'

    num_carnet = fields.Char('N° Carnet')
    state = fields.Selection([
    ('scratch', 'Brouillon'),
    ('in stock', 'En stock'),
    ], setting='Etat', readonly=True, default='scratch')
    creat_date = fields.Datetime('Date de création')
    first_utilisation_date = fields.Datetime("Date début d'utilisation")
    total_value = fields.Float('Valeur total')
    type_carnet = fields.Many2one('egov_ma.carnets.type', 'Type')
    vignette_id = fields.Many2many('egov_ma.hr.vignette', string='Vignette')


class EgovmacarnetsvignettesType(models.Model):
    _name = 'egov_ma.carnets.type'

    name = fields.Char('Nom')