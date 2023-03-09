from django.shortcuts import render
# from django.http import HttpResponse

from . import models


def index(request):
    tasks = models.Task.objects.all()
    context = {"tasks": tasks}

    return render(request, "todo/list.html", context)
