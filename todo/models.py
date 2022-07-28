from django.contrib.auth.models import User
from django.db import models


class ToDoModel(models.Model):
    class Meta:
        verbose_name= 'Tarefa'
        verbose_name_plural= 'Tarefas'
        
    autor = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name='Autor'
    )    
    data_de_criacao = models.DateTimeField(
        auto_now=True,
        verbose_name='Data da Tarefa'
    )
    tarefa = models.CharField(
        max_length=120,
        unique=False, 
        null=False, 
        blank=False, 
        verbose_name='Tarefa'
    )
    concluida = models.BooleanField(verbose_name='Concluído')
    
    def __str__(self) -> str:
        return self.tarefa
