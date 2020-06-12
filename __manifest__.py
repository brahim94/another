# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

{
    'name': 'egov_ma',
    'version': '13.0.1.2',
    'category': 'sale',
    'summary': 'egov_ma',
    'description': """
    egov_ma Hr enhancement in Odoo13.
    """,
    'author': 'Wizard Technolab',
    'website': 'http://www.wizardtechnolab.com',
    'depends': ['purchase', 'stock', 'fleet', 'hr', 'event'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequance_data.xml',
        'views/inherit_hr_department_view.xml',
        'views/inherit_event_event_view.xml',
        'views/inherit_hr_employee_view.xml',
        'views/egov_ma_department_type_view.xml',
        'views/egov_ma_event_trajets_view.xml',
        'views/inherit_hr_job_view.xml',
        'views/corp_grade_view.xml',
        'views/fleet_vignette.xml',
    ],
    'license': 'OPL-1',
}
