from django.urls import path  # , include
# from rest_framework import routers

from todo.views import apiOverview  # , TaskViewSet

# router = routers.DefaultRouter()
# router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path("", apiOverview),
    # path("api/", include(router.urls))
]
