from django.utils import timezone
from .models import Task, SubTask, Category
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'status', 'description', 'deadline']


class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'
        read_only_fields = ['created_at']


class CategoryCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        if Category.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError('Category already exists')

        return super().create(validated_data)


    def update(self, instance, validated_data):

        if Category.objects.filter(name=validated_data['name']).exclude(pk=instance.pk).exists():
            raise serializers.ValidationError('Category already exists')

        return super().update(instance, validated_data)


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_deadline(self, value):
        if value < timezone.now():
            raise serializers.ValidationError('Deadline cannot be in the past')
        return value




