from django import forms
from django.core.exceptions import ValidationError

from todo.models import ToDoModel


class ToDoForm(forms.ModelForm):
    class Meta:
        model= ToDoModel
        
        fields = [
            'tarefa',
        ]



    def clean_tarefa(self):
        text_task= self.cleaned_data.get('tarefa')
        if len(text_task) < 8:
            raise ValidationError(
            ('Tarefa não pode ter menos que 8 caracteres'),
            code='invalid',
        )
        return text_task
