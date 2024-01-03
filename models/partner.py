from odoo import api, fields, models

class PartnerExt(models.Model):
  _inherit = "res.partner"
  mobile = fields.Char(string='Mobile')
  id_no = fields.Char(string='ID / Passport no')
  country = fields.Char(string='Country')
