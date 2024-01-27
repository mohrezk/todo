from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from datetime import timedelta
from django.utils import timezone


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"

    def get_queryset(self):

        incomplete_tasks = Task.objects.filter(completed=False)
        review_tasks = Task.objects.filter(review__lte=timezone.localtime().date())


        for task in review_tasks:
            task.completed = False  
            task.review_time = None  
            task.save()  

        # return queryset | review_tasks
            
        queryset = incomplete_tasks.union(review_tasks)
        return queryset


class TaskDetailView(DetailView):
    model = Task


class UpdateTaskView(UpdateView):
    model = Task
    template_name = "tasks/task_update.html"
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("task-list")
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.object.completed:
            review_time = form.data.get('review_time')

            if review_time:
                print(1)
                self.object.review = timezone.now() + timedelta(days=int(review_time))

        self.object.save()
        return super().form_valid(form)
    

class CreateTaskView(CreateView):
    model = Task
    fields = ["title", "description"]
    success_url = reverse_lazy("task-list")


class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')