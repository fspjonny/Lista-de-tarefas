from django.urls import path

from .views import contact, index, new_user, sended

app_name='home'

urlpatterns = [
    path('', index, name='index'),
    path('registro/', new_user, name='registro'),
    path('registro/contato/', contact, name='contato'),
    path('registro/contato/sended/', sended, name='enviado'),
]
