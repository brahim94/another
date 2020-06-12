# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrDepartment(models.Model):
    _inherit = 'hr.department'

    type_unit_id = fields.Many2one('egov_ma.department.type', string='Type d’unité')
    ar_operating_unit = fields.Char(string='وحدة الإشتغال')
    is_type_root = fields.Boolean('Is Root', readonly=True)

    @api.onchange('type_unit_id')
    def _onchange_type_unit(self):
        if self.type_unit_id and self.type_unit_id.niveau == 'root':
            self.is_type_root = True
        else:
            self.is_type_root = False
