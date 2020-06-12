# -*- coding: utf-8 -*-
from odoo import fields, models, api


class EgovmadepartmentType(models.Model):
    _name = 'egov_ma.department.type'

    name = fields.Char('Nom', required=True)
    ar_name = fields.Char('الإسم')
    niveau = fields.Selection([('root', 'Root'), ('middle', 'Middle'), ('end', 'End')], 'Niveau', default='root')
