from django.urls import path
from . import views

app_name = 'soso'

urlpatterns = [
    path("login/", views.login),
]