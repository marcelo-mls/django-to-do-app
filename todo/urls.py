from django.urls import path  # , include
# from rest_framework import routers

import todo.views as views

# router = routers.DefaultRouter()
# router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("task-list/", views.taskList, name="task-list"),
    path("task-details/<str:pk>", views.taskDetails, name="task-details"),
    path("task-create/", views.taskCreate, name="task-create"),
    path("task-update/<str:pk>", views.taskUpdate, name="task-update"),
    path("task-delete/<str:pk>", views.taskDelete, name="task-delete"),
    # path("api/", include(router.urls))
]
