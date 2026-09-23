from django.urls import path
from .views import greeting

urlpatterns = [
    path("gr/", greeting, name="greeting"),
]
