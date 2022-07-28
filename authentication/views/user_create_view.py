from authentication.forms.form_cadadastro import RegisterForm
from authentication.forms.form_update import UpdateUserData
from django.shortcuts import redirect, render
from django.urls import reverse
from utils.utilities import makeUsernameLowerCase


def createUser(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(request, 'authentication/register.html', {
        'form':form,
        'form_action':reverse('authentication:createlogin')
        }
    )


def createLogin(request):
    if not request.POST:
        return redirect('authentication:logon')
    
    POST= request.POST
    request.session['register_form_data'] = POST
    request.session.set_expiry(300) #expira em 5 minutos
    form = RegisterForm(POST)

    if form.is_valid():
        data= form.save(commit=False)
        data.username=makeUsernameLowerCase(data.first_name+'_'+data.last_name)
        data.set_password(data.password)
        data.save()
        del(request.session['register_form_data'])
        return redirect('authentication:logon')
    return redirect('authentication:register')
