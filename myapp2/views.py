from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView


class TaskListView(ListView):
    model = Task
    template_name = 'myapp2/index.html'
    context_object_name = 'task_list'


class TaskCreateView(CreateView):
    model = Task
    fields = ('name', 'priority', 'date')
    template_name = 'myapp2/index2.html'
    success_url = reverse_lazy('index2')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'myapp2/delete.html'
    success_url = reverse_lazy('index2')


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'myapp2/edit.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk':self.object.pk})


class TaskDetailView(DetailView):
    model = Task
    template_name = 'myapp2/detail.html'
    context_object_name = 'task'
