# -*- coding: utf-8 -*-
{
    'name': "Reservas",

    'summary': """
        Reserva de clases y materiales por hora""",

    'description': """
        Modulo para la reserva y calculo del precio de clases por horas
    """,

    'author': "Grupo 2 - Yeray, Carlos, Erika, Daniel",
    'website': "http://www.grupo2-ssg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':'True',
}
