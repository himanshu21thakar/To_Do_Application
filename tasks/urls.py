from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add-task/", views.addTask, name="addTask"),
    path("delete-task/<int:id>/", views.delete_task, name="delete_task"),
    path("edit-task/<int:id>/", views.edit_task, name="edit_task"),
    path("mark-as-done/<int:pk>/", views.mark_as_done, name="mark_as_done"),
    path("mark-as-undone/<int:pk>/", views.mark_as_undone, name="mark_as_undone"),
]
