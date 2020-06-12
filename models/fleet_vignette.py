# -*- coding: utf-8 -*-
from odoo import fields, models, api


class FleetList(models.Model):
    _name = 'egov_ma.hr.vignette'
    #_inherit = 'fleet.vehicle'

    num_vingette = fields.Char('N° Vignette')
    amount = fields.Float('Montant')
    creat_date = fields.Datetime('Date de création')
    image = fields.Binary(attachment=True,
              help="This field holds the image used as vignette.")
    state = fields.Selection([
    ('available', 'Disponible'),
    ('affeted', 'Affecté'),
    ('used', 'Utilisé'),
    ], setting='State', readonly=True, default='available')