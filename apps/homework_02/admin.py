from django.contrib import admin
from .models import Task, Category, SubTask, Status


class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'short_title',
        'description',
        'status',
        'deadline',
        'created_at'
    )
    inlines = [SubTaskInline]

    def short_title(self, obj):
        if len(obj.title) > 10:
            return f'{obj.title[:10]}...'
        return obj.title


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'status',
        'deadline',
        'created_at'
    )

    def set_done(self, request, queryset):
        queryset.update(status=Status.DONE)

    actions = [set_done]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
