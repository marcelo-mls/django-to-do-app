from rest_framework.decorators import api_view
from rest_framework.response import Response

# from rest_framework import viewsets

from todo.models import Task
from todo.serializers import TaskSerializer

# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "List": "/task-list/",
        "Details": "/task-details/<str:pk>/",
        "Create": "/task-create/",
        "Update": "/task-update/<str:pk>/",
        "Delete": "/task-delete/<str:pk>/",
    }

    return Response(api_urls)


@api_view(["GET"])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def taskDetails(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)

    return Response(serializer.data)


@api_view(["POST"])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["PUT"])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response(f'Task {pk} deleted')
