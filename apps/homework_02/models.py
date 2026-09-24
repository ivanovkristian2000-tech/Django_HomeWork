from django.db import models


class Status(models.TextChoices):
    NEW = 'New', 'New'
    IN_PROGRESS = 'In progress', 'In progress'
    PENDING = 'Pending', 'Pending'
    BLOCKED = 'Blocked', 'Blocked'
    DONE = 'Done', 'Done'



class Task(models.Model):
    title = models.CharField(unique_for_date="created_at", max_length=100)
    description = models.TextField(max_length=500)
    categories = models.ManyToManyField('Category', related_name='tasks')
    status = models.CharField(max_length=20, choices=Status, default=Status.NEW)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

class SubTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    status = models.CharField(max_length=20, choices=Status, default=Status.NEW)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'