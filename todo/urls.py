from django.urls import path

from .views import create_task, delete_task, list, update_task

app_name='todo'

urlpatterns = [
    path('', list, name='list'),
    path('create/', create_task, name='create'),
    path('update/<int:id>/', update_task, name='update'),
    path('delete/<int:id>/', delete_task, name='delete'),
]
