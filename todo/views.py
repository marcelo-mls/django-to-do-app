from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import viewsets

from todo.models import Task


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


# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
