from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from .forms import TodoForm


def index(request):
    task_list = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')

        task = Task(name=name, priority=priority, date=date)
        task.save()

        return redirect(reverse_lazy('index'))

    return render(request, 'myapp/index.html', {'task_list':task_list})

def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method =="POST":
        task.delete()
        return redirect(reverse_lazy('index'))

    return render(request, 'myapp/delete.html', {'task':task})

def update(request, id):
    task = Task.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect(reverse_lazy('index'))
    return render(request, 'myapp/edit.html', {'form':form, 'task':task}) 













# def add(request):
#     if request.method == 'POST':
#         name = request.POST.get('name','')
#         priority = request.POST.get('priority', '')
#         task = Task(name=name, priority=priority)
#         task.save()
#         return redirect('/')

#     return render(request, "myapp/add.html")