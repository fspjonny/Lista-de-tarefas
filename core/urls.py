from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tarefas/admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('todo/', include('todo.urls'), name='todo'),
    path('login/', include('authentication.urls'), name='login'),
    path('recover/', include('recover.urls'), name='recover'),
]

handler404 = "home.views.handler404"
