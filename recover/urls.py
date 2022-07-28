from django.contrib.auth import views as auth_views
from django.urls import include, path

from recover.views import MyPasswordResetConfirmView, MyPasswordResetView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('reset-password/', MyPasswordResetView.as_view(
        template_name='recover/password_reset.html'), 
         name='reset_password'
    ),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='recover/password_reset_done.html'), 
         name='password_reset_done'
    ),
    path('reset/<uidb64>/<token>/', 
         MyPasswordResetConfirmView.as_view(
             template_name='recover/password_reset_confirm.html'), 
         name='password_reset_confirm'
    ),
    path('reset-password-complete/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='recover/password_reset_confirm_done.html'), 
         name='password_reset_complete'
    ),    
]
