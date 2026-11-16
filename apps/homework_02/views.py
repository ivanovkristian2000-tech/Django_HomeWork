from django.utils import timezone

from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


@api_view(['POST'])
def post_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_task_list(request):
    try:
        tasks = Task.objects.all()
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_tasks(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_task_statistics(request):
    all_tasks_count = Task.objects.all().count()
    status_count = Task.objects.values('status').annotate(count=Count('id'))
    overdue_count = Task.objects.filter(deadline__lt=timezone.now()).count()
    return Response({
        'all_tasks_count': all_tasks_count,
        'status_count': status_count,
        'overdue_count': overdue_count,
    })



