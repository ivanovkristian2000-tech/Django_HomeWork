import os
import django
from datetime import date, timedelta
from django.utils import timezone


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


from apps.homework_02.models import Task, SubTask, Category, Status


tasks = Task.objects.create(
    title="Prepare presentation",
    description="Prepare materials and slides for the presentation",
    status=Status.NEW,
    deadline=timezone.now() + timedelta(days=3),
)

subtask = SubTask.objects.create(
    task=tasks,
    title="Gather information",
    description="Find necessary information for the presentation",
    status=Status.NEW,
    deadline=timezone.now() + timedelta(days=2),
)

subtask_2 = SubTask.objects.create(
    task=tasks,
    title="Create slides",
    description="Create presentation slides",
    status=Status.NEW,
    deadline=timezone.now() + timedelta(days=1),
)

tasks_status_new = Task.objects.filter(status=Status.NEW)
for task in tasks_status_new:
    print(task)

subtasks_status_done = SubTask.objects.filter(
    status=Status.DONE,
    deadline__lt=timezone.now()
)
for subtask in subtasks_status_done:
    print(subtask)

task = Task.objects.filter(title="Prepare presentation").update(
    status=Status.IN_PROGRESS
)

subtask_update_deadline = SubTask.objects.filter(title="Gather information").update(
    deadline=timezone.now() - timedelta(days=2)
)

subtasks_update_description = SubTask.objects.filter(title="Create slides").update(
    description="Create and format presentation slides"
)

delete_task = Task.objects.filter(title="Prepare presentation").delete()
