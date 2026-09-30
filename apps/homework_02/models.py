from django.db import models
from django.db.models import UniqueConstraint


class Status(models.TextChoices):
    NEW = 'New', 'New'
    IN_PROGRESS = 'In progress', 'In progress'
    PENDING = 'Pending', 'Pending'
    BLOCKED = 'Blocked', 'Blocked'
    DONE = 'Done', 'Done'


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    categories = models.ManyToManyField('Category', related_name='tasks')
    status = models.CharField(max_length=20, choices=Status, default=Status.NEW)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'task_manager_task'
        verbose_name = 'Task'
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_task_title')
        ]


class SubTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    status = models.CharField(max_length=20, choices=Status, default=Status.NEW)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'task_manager_subtask'
        verbose_name = 'SubTask'
        ordering = ['-created_at']
        constraints = [
            UniqueConstraint(fields=['title'], name='unique_subtask_title')
        ]


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'Category'
        constraints = [
            UniqueConstraint(fields=['name'], name='unique_category_name')
        ]
