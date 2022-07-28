from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       PasswordResetForm, SetPasswordForm)


class MyPasswordResetForm(PasswordResetForm):
    
    email = forms.EmailField(
    label="",
    max_length=254,
    widget=forms.EmailInput(
        attrs={
            "class":"input-field",
            "autocomplete": "email",
            "placeholder": "Seu email de cadastro",
            }
        ),
    )

        
class MySetPasswordForm(SetPasswordForm):

    error_messages = {
        "password_mismatch": "Os dois campos de senha não correspondem.",
    }
    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class":"input-field",
                "autocomplete": "new-password",
                "placeholder": "nova senha",
                }
            ),
        strip=False,
        help_text="",
    )
    new_password2 = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class":"input-field",
            "autocomplete": "new-password",
            "placeholder": "repita a nova senha",
            }
        ),
    )
    