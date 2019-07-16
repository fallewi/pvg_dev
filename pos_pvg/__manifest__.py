# -*- coding: utf-8 -*-


{
    'name': 'POS PVG',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Extensions for the Point of Sale ',
    'description': "",
    'depends': ['point_of_sale'],
    'website': '',
    'data': [
        'security/ir.model.access.csv',
        'views/pos_sales_cost_report.xml',
        'views/pos_sales_cost_report_line.xml',
        'views/pos_customer_orders_report.xml',
        'views/pos_customer_orders_report_line.xml',
        'reports/pos_sales_cost_report.xml',
        'reports/pos_customer_orders_report.xml',
        'wizard/pos_customers_orders_report.xml',
    ],
    'installable': True,
    'auto_install': False,
}
