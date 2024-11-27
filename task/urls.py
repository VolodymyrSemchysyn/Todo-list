from django.urls import path

from task.views import TaskListView, TagListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TagCreateView, \
    TagUpdateView, TagDeleteView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task_create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("tags/create/", TagCreateView.as_view(), name="tag_create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag_update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),

]

app_name = "tasks"