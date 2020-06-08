from django.shortcuts import render,  redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.core import serializers
from .models import TODO
from .forms import TodoForm
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def to_do(request):
    '''
Here, it checks whether the user has passed any request to the server if None then return top 6 upcoming events 
near to the deadline

    '''
    if request.GET.get('q') == None:
        to_do = TODO.objects.filter(
        deadline__day__gte=datetime.datetime.now().day,

        deadline__year = datetime.datetime.now().year,

        deadline__month__gte = datetime.datetime.now().month).order_by('deadline')[:6]
        context = {'to_do':to_do}
        return render(request, 'todo/to_do.html',context)
    else:
        q = request.GET.get('q', None)
        items = ''
        if q is None or q is "":
            to_do = TODO.objects.filter(
        deadline__day__gte=datetime.datetime.now().day,

        deadline__year = datetime.datetime.now().year,

        deadline__month__gte = datetime.datetime.now().month).order_by('deadline')[:6]
            
        elif q is not None:
            to_do = TODO.objects.filter(text__contains=q)
        auth_mod = None
        if len(TODO.objects.all()) >= 1:
            auth_mod = True
        context = {'to_do':to_do, 'auth_mod': auth_mod}
        return render(request, 'todo/to_do.html',context)
    
    
@login_required
def update_form(request, todo_id):
    todo = get_object_or_404(TODO, pk=todo_id)
    form = TodoForm(instance = todo)
    if request.user.is_authenticated:
        form = TodoForm(instance = todo)
        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data['text']
                deadline = form.cleaned_data['deadline']
                todo.deadline = deadline
                todo.text = text
                todo.save()
                return redirect('todo')
    context = {'form':form}
    return render(request, 'todo/update_form.html',context)
@login_required
def create_form(request):
    form = TodoForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                form= form.save(commit=False)
                form.user = request.user
                print(form.user)
                form.save()
                return redirect('todo')
    else:
        if request.method == 'POST':
            
            form = TodoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('todo')
    context = {'form':form}
    return render(request, 'todo/create_form.html',context)

def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            form.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('create_task')
    context = {'form':form}
    return render(request, 'todo/sign_up.html', context)
@login_required
def delete_todo(request):
    import json
    data =json.loads(request.body)
    todo = get_object_or_404(TODO ,pk=int(data['todo_id']))
    todo.delete()
    return JsonResponse('Item deleted', safe=False)

