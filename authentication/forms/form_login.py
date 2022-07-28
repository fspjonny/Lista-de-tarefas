from django import forms


class LoginForm(forms.Form):
    
    email= forms.CharField(
        required=True,
        widget= forms.EmailInput(
            attrs={
                'class':'input-field',
                'placeholder':'Seu email',
            }
        )
    )

    password= forms.CharField(
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'class':'input-field',
                'placeholder':'Sua senha',
            }
        )
    )
