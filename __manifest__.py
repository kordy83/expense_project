{
    'name': 'Expense Project Inherit',
    'version': '1.0.0',
    'summary': '',
    'description': 'edit on project module and expense module',
    'depends': [
        'base',
        'hr_expense',
        'project',
        "sale",
        "sale_project",
    ],
    'data': [
        'views/project_task_view.xml',
        'views/hr_expense_view.xml',
        'views/hr_expense_sheet_view.xml',
    ]

}
