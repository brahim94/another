# -*- coding: utf-8 -*-
from odoo import fields, models, api


class EventEvent(models.Model):
    _inherit = 'event.event'

    conducteur_id = fields.Many2one('hr.employee', string="Conducteur")
    vehicle_id = fields.Many2one('fleet.vehicle', string="véhicule")
    trajets_ids = fields.Many2many('egov_ma.event.trajets', 'event_trajets_rel', 'event_id', 'trajet_id', string="Trajet")
    num_serie  = fields.Char('N° de série')
    objet_txt = fields.Text('Objet')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('event.event.sequence')
        return super(EventEvent, self).create(vals)


class EgovmaEventTrajets(models.Model):
    _name = 'egov_ma.event.trajets'

    name = fields.Char('Nom', readonly=True)
    type = fields.Selection([('route_nationale', 'Route Nationale'), ('autoroute', 'Autoroute')], 'Type',
                            default='route_nationale')
    _sql_constraints = [        
    ('type_uniq',
        'UNIQUE (type)',
        'type must be unique.')
    ]
    starting_point_id = fields.Many2one('egov_ma.event.emplacement', string='Point de départ')
    _sql_constraints = [        
    ('starting_point_uniq',
        'UNIQUE (starting_point_id)',
        'starting point must be unique.')
    ]
    arrival_point_id = fields.Many2one('egov_ma.event.emplacement', string='Point de arrivée')
    _sql_constraints = [        
    ('arrival_point_uniq',
        'UNIQUE (arrival_point_id)',
        'arival point must be unique.')
    ]
    km_estimated = fields.Float('KM Estimé')
    charge_auto = fields.Float('Frais Autoroute')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('event.trajets.sequence')
        return super(EgovmaEventTrajets, self).create(vals)


class EgovmaEventEmplacement(models.Model):
    _name = 'egov_ma.event.emplacement'

    name = fields.Char('Nom', required=True)
    ar_name = fields.Char('نام')


class EgovmaEventTrajetsRetour(models.Model):
    _inherit = 'event.event'

    trajets_idss = fields.Many2many('egov_ma.event.trajets', 'event_trajets_rel', 'event_id', 'trajet_id', string="Trajets Retour")
