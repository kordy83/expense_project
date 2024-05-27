from odoo import api, fields, models


class HrExpense(models.Model):
    _inherit = 'hr.expense'

    project_id = fields.Many2one('project.project', string='Project Name')
    task_id = fields.Many2one('project.task', string='Task Name',
                              domain="[('project_id', '=', project_id),('task_expenses', '=', 'yes')]")

    task_expense_sponsor = fields.Selection(related='task_id.task_expenses', readonly=1, string='Task Expenses')
    task_expenses_label = fields.Selection(related='task_id.expenses_label', readonly=1, string='Client Or Oditlz')

    task_sale_line_id_order_id = fields.Integer(compute='_compute_task_sale_line_id_order_id', invisible=1)
    partner_id = fields.Many2one('res.partner', string='Customer')


    @api.depends('partner_id', 'sale_order_id')
    def _compute_task_sale_line_id_order_id(self):
        for rec in self:
            rec.task_sale_line_id_order_id = self.task_id.sale_line_id.order_id.id

