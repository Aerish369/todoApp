from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
# Create your views here.

@login_required(login_url='user-login')
def tasks(request):
    profile = request.user.profile
    tasks = profile.task_set.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = profile
            task.save()
            return redirect('tasks')
    context = { 
        'tasks': tasks,
        'form': form,
     }
    return render(request, 'todoApp/tasks.html', context)


@login_required(login_url='user-login')
def viewTask(request, pk):
    profile = request.user.profile
    tasks = profile.task_set.get(id=pk)
    context = {
        'tasks':tasks
    }
    return render(request, 'todoApp/view-task.html', context)



@login_required(login_url='user-login')
def updateTasks(request, pk):
    profile = request.user.profile
    tasks = profile.task_set.get(id=pk)
    form = TaskForm(instance=tasks)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    context = {
        'form': form,
        'tasks': tasks,
    }
    return render(request, 'todoApp/form.html', context)
 

@login_required(login_url='user-login')
def deleteTasks(request, pk):
    profile = request.user.profile
    tasks = profile.task_set.get(id=pk)
    if request.method == 'POST':
        tasks.delete()
        return redirect('tasks')
    context = {
        'tasks': tasks,
    }
    return render(request, 'todoApp/delete-tasks.html', context)