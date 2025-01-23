from django.contrib.admin.widgets import url_params_from_lookup_dict
from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("actors", ActorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
