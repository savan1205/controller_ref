from odoo import  http
from odoo.http import request

class CustomPortal(http.Controller):

	@http.route('/employees', type='http', auth="public", website=True)
	def portal_controller(self,**kw):
		employees = request.env['hr.employee'].search([])
		return request.render('practice_module.employees_from_controllers',{'employees':employees})

	@http.route('/employee/<model("hr.employee"):employee>', type='http', auth="public", website=True)
	def employee_details(self,employee,**kw):
		return request.render('practice_module.employees_details',{'employee':employee})

