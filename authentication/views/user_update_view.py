from authentication.forms.form_update import UpdateUserData
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from utils.utilities import makeUsernameLowerCase


@login_required(login_url='authentication:logon', redirect_field_name='next')
def user_settings(request):
  data_user=get_object_or_404(User.objects.filter(pk=request.user.pk))
  form_user = UpdateUserData(request.POST or None, instance=data_user)
  
  prevent_password = data_user.password
  
  if form_user.is_valid():
    new_data = form_user.save(commit=False)
    if new_data.password !='':
      new_data.set_password(new_data.password)
    else:
      new_data.password= prevent_password
    new_data.username= makeUsernameLowerCase(
      new_data.first_name+'_'+new_data.last_name
    )  
    new_data.save()
    messages.success(request, 'Dados Atualizados!')
    return redirect('authentication:settings')
  

  return render(request, 'authentication/user_settings.html', {
    'form_user':form_user,
    'form_action':reverse('authentication:settings'),
    }
  )
