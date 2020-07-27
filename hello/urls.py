from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("rishi", views.rishi, name="rishi"),
    path("<str:name>", views.greet, name="greet")
]
