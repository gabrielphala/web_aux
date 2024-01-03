from odoo import api, fields, models

class Beneficiary(models.Model):
  _name = "web_aux.beneficiaries"
  _description = "List of all benefeciaries"

  name = fields.Char(string='Name')
  mobile = fields.Char(string='Mobile')
  city = fields.Char(string='City')
  country = fields.Char(string='Country')
