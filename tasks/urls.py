from django.urls import path
from .views import TaskListView, TaskDetailView, CreateTaskView, UpdateTaskView, DeleteTaskView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("edit/<int:pk>/", UpdateTaskView.as_view(), name="task-update"),
    path("add/", CreateTaskView.as_view(), name='task-create'),
    path("delete/<int:pk>", DeleteTaskView.as_view(), name="task-delete"),
]
