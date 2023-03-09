from django.shortcuts import render, redirect

from . import models
from . import forms


def index(request):
    tasks = models.Task.objects.all()
    form = forms.TaskForm()

    if request.method == "POST":
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {"tasks": tasks, "form": form}
    return render(request, "todo/list.html", context)


def updateTask(request, pk):
    task = models.Task.objects.get(id=pk)
    form = forms.TaskForm(instance=task)

    if request.method == "POST":
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {"form": form}
    return render(request, "todo/update.html", context)
