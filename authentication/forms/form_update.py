from collections import defaultdict

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.utilities import strong_password


class UpdateUserData(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.listerrors= defaultdict(list)
    
    password = forms.CharField(
        required=False,
        widget= forms.PasswordInput(
            attrs={
                'class':'input-field',
                'placeholder':'Digite uma senha forte',
                'minlength':8,
                'type':'password',
            }
        ),
        validators=[strong_password],
        label='Senha',
    )
    
    password_confirm = forms.CharField(
        required=False,
        widget= forms.PasswordInput(
            attrs={
                'class':'input-field',
                'placeholder':'Repita a senha digitada',
                'minlength':8,    
                'type':'password',
            }
        ),
        validators=[strong_password],
        label='Confirmar senha',
    )
    
    class Meta:
        model= User
        
        fields= [
            'first_name',
            'last_name',
            'password',
        ]
       
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class':'input-field',
                    'placeholder':'Seu nome',
                    'minlength':3,
                    'required':True,
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'class':'input-field',
                    'placeholder':'Seu sobrenome',
                    'minlength':10,
                    'required':True,
                }
            ),
        }


# VALIDAÇÃO DE CAMPOS

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        
        clean_data= self.cleaned_data
        
        name= clean_data.get('first_name')
        lastname= clean_data.get('last_name')
        password= clean_data.get('password')
        password_confirm= clean_data.get('password_confirm')
        
        
        if len(name) < 3:
            self.listerrors['name'].append(
                'Primeiro nome deve ter 3 ou mais caracteres'
                )

        if len(lastname) < 5:
            self.listerrors['last_name'].append(
                'Sobrenome deve ter 5 ou mais caracteres'
                )
       
        if password != password_confirm:
            self.listerrors['password'].append(
                'Senhas digitadas são diferentes!'
                )
            self.listerrors['password_confirm'].append(
                'Senhas digitadas são diferentes!'
                )


        if self.listerrors:
            raise ValidationError(self.listerrors)
        
        return super_clean
        
