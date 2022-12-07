from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('eventhome/',views.eventhome, name='eventhome'),
]
