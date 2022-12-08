from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),
    path("follow/<str:username>/", views.follow, name="follow"),
    path("profile/<str:username>/", views.profile, name="profile"),
]
