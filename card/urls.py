from django.urls import path
from . import views

app_name = 'card'

urlpatterns = [
    path('detail/<int:num>', views.detail, name="detail"),
    path('search/',views.search, name='search'),
    path('comment/<int:pk>', views.comment, name="comment")
]