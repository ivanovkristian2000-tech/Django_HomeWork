from apps.homework_02.views import get_task_list, get_tasks, post_task, get_task_statistics
from django.urls import path


urlpatterns = [
    path('addtask/', post_task, name='post_task'),
    path('tasks/', get_task_list, name='get_task_list'),
    path('task/<int:pk>/', get_tasks, name='get_tasks'),
    path('task-statistics/', get_task_statistics, name='get_task_statistics'),
]


