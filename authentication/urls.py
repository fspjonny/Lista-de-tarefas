from django.urls import path

from authentication.views.login_view import (login_verification, logon_view,
                                             logout_view)
from authentication.views.user_create_view import createLogin, createUser
from authentication.views.user_update_view import user_settings

app_name='authentication'

urlpatterns = [
    path('', logon_view, name='logon'),
    path('register/', createUser, name='register'),
    path('create/', createLogin, name='createlogin'),
    path('autorization/', login_verification, name='login_verification'),
    path('logout/', logout_view, name='logout'),
    path('settings/', user_settings, name='settings'),
]
