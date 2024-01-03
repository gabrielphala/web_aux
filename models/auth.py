from odoo.addons.auth_signup.controllers.main import AuthSignupHome

class AuthSignupExt(AuthSignupHome):
  def _signup_with_values(self, token, values):
    context = self.get_auth_signup_qcontext()

    values.update({
      'mobile': context.get('mobile'),
      'id_no': context.get('id_no'),
      'country': context.get('country')
    })

    super(AuthSignupExt, self)._signup_with_values(token, values)