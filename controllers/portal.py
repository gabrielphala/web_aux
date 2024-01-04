from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request
from odoo import http

class WebAuxPortal(CustomerPortal):
  @http.route(['/new/beneficiary'], type='http', auth='public', website=True)
  def newBeneficiaryForm (self, **kw):
    if (request.httprequest.method == 'POST'):
      request.env['web_aux.beneficiaries'].create({
        'name': kw.get('name'),
        'mobile': kw.get('mobile'),
        'city': kw.get('city'),
        'country': kw.get('country'),
        'user_id': request.env.user.id
      })

      print(kw)

    vals = {'page_name': 'new_beneficiary'}
    return request.render('web_aux.new_beneficiary', vals)

  @http.route(['/my/beneficiaries'], type='http', auth='public', website=True)
  def beneficiaryListView(self, **kw):
    vals = { 'page_name': 'beneficiaries', 'beneficiaries': request.env['web_aux.beneficiaries'].search([('user_id', '=', request.env.user.id)])}

    return request.render('web_aux.beneficiary_list', vals)

  @http.route(['/my/beneficiary'], type='http', auth='public', website=True)
  def viewBeneficiary(self, **kw):
    vals = { 'beneficiary': request.env['web_aux.beneficiaries'].search([('id', '=', kw.get('id'))], limit=1)}

    if (request.httprequest.method == 'POST'):
      request.env['web_aux.beneficiaries'].search([('id', '=', kw.get('id'))], limit=1).write({
        'name': kw.get('name'),
        'mobile': kw.get('mobile'),
        'city': kw.get('city'),
        'country': kw.get('country')
      })

    return request.render('web_aux.view_beneficiary', vals)

  @http.route(['/shop/beneficiaries'], type='http', auth='public', website=True)
  def beneficiaryShopListView(self, **kw):
    vals = { 'beneficiaries': request.env['web_aux.beneficiaries'].search([('user_id', '=', request.env.user.id)])}

    print("Shop beneficiaries")

    return request.render('web_aux.shop_beneficiary_list', vals)