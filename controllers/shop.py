from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request, Response
from odoo import http, fields

class WebAuxSale(WebsiteSale):
    @http.route(['/shop/select/beneficiary'], type='json',  auth="public", csrf=False)
    def selectBeneficiary(self, **kw):
        request.session['beneficiary_id'] = request.params['beneficiary_id']

        return 'done'
    
    @http.route(['/shop/pay'], type='http', auth="public", website=True, sitemap=False)
    def shopPay(self, access_token=None, revive='', **post):
        """
        Main cart management + abandoned cart revival
        access_token: Abandoned cart SO access token
        revive: Revival method when abandoned cart. Can be 'merge' or 'squash'
        """
        order = request.website.sale_get_order()
        if order and order.state != 'draft':
            request.session['sale_order_id'] = None
            order = request.website.sale_get_order()

        request.session['website_sale_cart_quantity'] = order.cart_quantity

        values = {}

        print("Beneficiary: ", request.session['beneficiary_id'])

        values.update({
            'website_sale_order': order,
            'beneficiary': request.env['web_aux.beneficiaries'].search([('id', '=', request.session['beneficiary_id'])], limit=1),
            'date': fields.Date.today(),
            'suggested_products': [],
        })

        return request.render("web_aux.shop_payment", values)
