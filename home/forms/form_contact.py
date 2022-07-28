from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=80,
        required=True,
        widget= forms.TextInput(
            attrs={
                'class':'input-field',
                'placeholder':'Nome',
                'type':'text',
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget= forms.EmailInput(
            attrs={
                'class':'input-field',
                'placeholder':'E-mail',
                'type':'email',
            }
        ),
    )
    message = forms.CharField(
        required=True,
        widget= forms.TextInput(
            attrs={
                'class':'input-field',
                'placeholder':'Sua mensagem',
                'type':'text',
            }
        )
    )
    
    def get_info(self):
        clean_data = super().clean()
        
        name = clean_data.get('name').strip()
        from_mail = clean_data.get('email')
        message = f"{name} entrou em contato com o e-mail: {from_mail} e disse:"
        message+= f"\n{clean_data.get('message')}"
        
        return message
