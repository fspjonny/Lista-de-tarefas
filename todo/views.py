from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ToDoForm
from .models import ToDoModel


@login_required(login_url='authentication:logon', redirect_field_name='next')
def list(request):
    lista_tarefas = ToDoModel.objects.filter(
        autor=request.user.id
        ).order_by('concluida','-data_de_criacao')

    data_in_session = request.session.get('register_form_data', None)    
    form = ToDoForm(data_in_session)
    return render(request, 'todo/todo_list.html',{
        'form':form,
        'form_action':reverse('todo:list'),
        'lista':lista_tarefas,
    })


@login_required(login_url='authentication:logon', redirect_field_name='next')
def create_task(request):
    if not request.POST:
        raise Http404()
    
    sended_post = request.POST
    request.session['register_form_data'] = sended_post
    form = ToDoForm(sended_post)
    
    if form.is_valid():
        data = form.save(commit=False)
        no_space= data.tarefa.strip()
        duplicated_data = ToDoModel.objects.filter(
            autor=request.user,
            tarefa=no_space
        )
        occurrence = len(duplicated_data)
        
        if occurrence >= 1:
            messages.warning(request, 'Esta tarefa já está cadastrada!')
            del(request.session['register_form_data'])
            return redirect(reverse('todo:list'))
        else:
            data.autor=request.user
            data.concluida=False
            data.save()
        
            messages.success(request, 'Tarefa adicionada!')
            del(request.session['register_form_data'])
        
            return redirect(reverse('todo:list'))
    else:
        messages.error(request, form.errors['tarefa'][0])
      
        del(request.session['register_form_data'])
        return redirect(reverse('todo:list'))
        

@login_required(login_url='authentication:logon', redirect_field_name='next')
def update_task(request, id):
    tarefa = get_object_or_404(ToDoModel, pk=id)
    
    if tarefa.concluida:
        tarefa.concluida=False
        tarefa.save()
        return redirect('todo:list')
    else:
        tarefa.concluida=True
        tarefa.save()
        return redirect('todo:list')


@login_required(login_url='authentication:logon', redirect_field_name='next')
def delete_task(request, id):
    tarefa = get_object_or_404(ToDoModel, pk=id)
    tarefa.delete()
    return redirect('todo:list')
