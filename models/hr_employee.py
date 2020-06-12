# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    first_name = fields.Char('Prénom')
    last_name = fields.Char('nom de famille')
    ar_first_name = fields.Char('الإسم')
    ar_last_name = fields.Char('اللقب')
    ar_name = fields.Char('الإسم الكامل')
    corps = fields.Many2one('egov_ma.hr.corp', string='Corps')
    grade = fields.Many2one('egov_ma.hr.grade', string='Grade')
    nu_cin = fields.Char('N° de CIN')
    num_ppr = fields.Char('N °PPR ')
    objet_txt = fields.Text('Objet')


    @api.onchange('first_name', 'last_name')
    def onchange_name_concatenation(self):
        if self.first_name or self.last_name:
            f_name = self.first_name if self.first_name else ''
            l_name = self.last_name if self.last_name else ''
            self.name = f_name + ' ' + l_name

    @api.onchange('ar_first_name', 'ar_last_name')
    def onchange_ar_name_concatenation(self):
        if self.ar_first_name or self.ar_last_name:
            ar_f_name = self.ar_first_name if self.ar_first_name else ''
            ar_l_name = self.ar_last_name if self.ar_last_name else ''
            self.ar_name = ar_f_name + ' ' + ar_l_name


class EgovmaHrCorp(models.Model):
    _name = 'egov_ma.hr.corp'

    name = fields.Char('Nom', required=True)
    ar_name = fields.Char('نام')


class EgovmaHrGrade(models.Model):
    _name = 'egov_ma.hr.grade'

    name = fields.Char('Nom', required=True)
    ar_name = fields.Char('نام')


class EgovmaHrJob(models.Model):
    _inherit = 'hr.job'

    ar_name = fields.Char('المنصب')
