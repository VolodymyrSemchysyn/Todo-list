from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from task.forms import TaskForm, TagForm
from task.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 4

    def get_queryset(self):
        return Task.objects.all().order_by("is_done", "-created_at").prefetch_related("tags")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 3

    def get_queryset(self):
        return Tag.objects.prefetch_related("tasks").all()


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tags")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tags")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tags")
