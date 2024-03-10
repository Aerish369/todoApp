from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'), 
    path('view-task/<str:pk>/', views.viewTask, name='view-task'),
    path('update-tasks/<str:pk>/', views.updateTasks, name='update-tasks'),
    path('delete-tasks/<str:pk>/', views.deleteTasks, name='delete-tasks'),
]
