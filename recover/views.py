from django.contrib.auth.views import (PasswordResetConfirmView,
                                       PasswordResetView)

from recover.forms import MyPasswordResetForm, MySetPasswordForm


class MyPasswordResetView(PasswordResetView):
    form_class = MyPasswordResetForm
    email_template_name = "recover/password_reset_email.html"
    


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = MySetPasswordForm
