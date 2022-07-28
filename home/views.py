from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse

from home.forms.form_contact import ContactForm
from home.forms.form_register import RegisterUserForm


def index(request):
    form_contact = ContactForm()
    return render(request, 'home/index.html',{
        'form_contact':form_contact,
        'contact':reverse('home:contato')
        }
    )

def new_user(request):
    if request.POST:
        form_new_user= RegisterUserForm(request.POST)
    else:    
        form_new_user= RegisterUserForm()
    return render(request, 'home/form_user.html',{'userForm':form_new_user})

def handler404(request, exception):
    return render(request, 'home/page_error.html')


def contact(request):
    if not request.POST:
        return redirect('home:index')
 
    form = ContactForm(request.POST)
  
    if form.is_valid():
        subject= "Contato via App Tarefas."
        message= f"Mensagem enviada por {form.cleaned_data.get('name')},"
        message+= f"\nE-mail: {form.cleaned_data.get('email')}"
        message+= f"\n\n{form.cleaned_data.get('message')}"
        message+= "\n\n Via App Tarefas!"
        recipient= [settings.EMAIL_HOST_USER,]
        send_mail(
            subject=subject, 
            message=message,
            from_email=form.cleaned_data.get('email'),
            recipient_list=recipient, 
            fail_silently=False,
        )
        messages.success(request, 'Sua mensagem foi enviada com sucesso!')
        return redirect('home:enviado')

def sended(request):
    return render(request, 'home/email_success.html')
