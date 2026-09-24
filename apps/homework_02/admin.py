from django.contrib import admin
from .models import Task, Category, SubTask


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'status',
        'deadline',
        'created_at'
    )

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'status',
        'deadline',
        'created_at'
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
