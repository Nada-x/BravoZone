from django.urls import path
from evaluation import views


app_name="evaluation"

urlpatterns = [
      path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
]