from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.


def tasks(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    context = { 
        'tasks': tasks,
        'form': form,
     }
    return render(request, 'todoApp/tasks.html', context)


def viewTask(request, pk):
    tasks = Task.objects.get(id=pk)
    context = {
        'tasks':tasks
    }
    return render(request, 'todoApp/view-task.html', context)



def updateTasks(request, pk):
    tasks = Task.objects.get(id=pk)
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
 

def deleteTasks(request, pk):
    tasks = Task.objects.get(id=pk)
    if request.method == 'POST':
        tasks.delete()
        return redirect('tasks')
    context = {
        'tasks': tasks,
    }
    return render(request, 'todoApp/delete-tasks.html', context)