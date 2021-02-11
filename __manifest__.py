# -*- coding: utf-8 -*-
{
    'name': "proydefinitivo",

    'summary': """
        Proyecto definitivo
    """,

    'description': """
    Este proyecto es el definitivo despues de muchos problemas
    """,

    'author': "Jose Maria Pinha Garcia",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/definitivo.xml',
        'views/pedido.xml',
        'views/suceso.xml',
        'views/lineapedido.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
