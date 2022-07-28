from authentication.forms.form_login import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse


def logon_view(request):
    login_form = LoginForm()
    return render(request, 'authentication/login.html',{
        'login_form':login_form,
        'form_verification':reverse('authentication:login_verification'),
        }
    )


def login_verification(request):
    if not request.POST:
        return redirect('authentication:logon')
    
    login_form_data = LoginForm(request.POST)

    if login_form_data.is_valid():
        authenticated_user= authenticate(
            username=login_form_data.cleaned_data.get('email',''),
            password=login_form_data.cleaned_data.get('password',''),
        )

        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect('todo:list')
        else:
            messages.error(request, 'Dados incorretos!')
            return redirect('authentication:logon')
    else:
        messages.error(request, 'Dados incorretos!')
        return redirect('authentication:logon')


@login_required(login_url='authentication:logon', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('home:index'))
    
    if request.POST.get('username') != request.user.username:
        return redirect(reverse('todo:list'))
        
    logout(request)
    return redirect(reverse('home:index'))
