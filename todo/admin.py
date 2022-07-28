from django.contrib import admin

from .models import ToDoModel


#Classe ToDoAdmin, escolha o que exibir ou omitir no Admin:
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('data_de_criacao', 'tarefa', 'concluida', 'autor')
    list_filter = 'data_de_criacao','concluida'
    search_fields = 'tarefa__contains',
    list_display_links = 'tarefa',
    list_per_page = 10


#Registrando o Model e a Classe Admin
admin.site.register(ToDoModel, ToDoAdmin)
