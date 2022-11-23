{
    'name': 'Practice',
    'version': '15.0.1',
    'category': 'Practice Module',
    'summary': 'Practice Module',
    'sequence': -500,
    'description': """
This module contains all the common features of for practice(currently for controllers).
    """,
    'depends': ['sale','website'],
    'data': [
        'report/custom_sale_report.xml',
        'report/header_inherit.xml',
        'report/report_custom_so_action.xml',

        'views/customer_dashboard_task_view.xml',
        'views/controller_template.xml',

    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    
       
    'license': 'LGPL-3',

}
