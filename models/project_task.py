from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _inherit = 'project.task'
    pay_state_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    states_choices = [
        ('included', 'Included'),
        ('excluded', 'Excluded'),
    ]
    task_expenses_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    expenses_label_choices = [
        ('client', 'Client'),
        ('oditlz', 'Oditlz'),
    ]
    pay_state = fields.Selection(pay_state_choices, string='Is Paid?')
    states = fields.Selection(states_choices, string='Status')

    task_expenses = fields.Selection(task_expenses_choices, string=' ')
    expenses_label = fields.Selection(expenses_label_choices, string=' ', default='client')

    product_id = fields.Many2one('product.product', string='Add New Product')

    product_quantity = fields.Integer(default=1)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        data = {}
        for rec in self:
            if rec.sale_line_id.order_id.id is False:
                data = {
                    'warning': {
                        'title': 'Warning',
                        'message': "You Must Select 'Sales Order Item'",
                        "type": "notification"
                    }
                }
        return data

    def add_product_to_sale_order(self):
        try:
            for task in self:
                task.env['sale.order.line'].create({
                    'order_id': task.sale_line_id.order_id.id,
                    'product_id': task.product_id.id,
                    'product_uom_qty': task.product_quantity,
                })
        except:
            raise ValidationError("You Must Fill 'Sales Order Item' And 'Add New Product'")

    def action_create_sale_order(self):
        action = self.env['ir.actions.actions']._for_xml_id('sale.action_orders')
        view_id = self.env.ref('sale.view_order_form').id

        action['views'] = [[view_id, 'form']]
        return action
