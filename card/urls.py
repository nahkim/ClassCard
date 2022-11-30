from django.urls import path
from . import views

app_name = 'card'

urlpatterns = [
    path('detail/<int:num>', views.detail, name="detail"),
]