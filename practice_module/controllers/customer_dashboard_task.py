from odoo import  http
from odoo.http import request

class CustomerDashboard(http.Controller):

	@http.route('/sale/order', type='http', auth="public", website=True)
	def customer_controller(self,**kw):
		saleorders = request.env['sale.order'].search([])
		return request.render('practice_module.order_dashboard_from_controllers',{'saleorders':saleorders})

