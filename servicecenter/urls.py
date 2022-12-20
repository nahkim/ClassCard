from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('',views.index, name='index'),
    path('create/',views.create, name='create'),
    path('<int:pk>/',views.detail, name='detail'),
    path('comment_delete/<int:service_pk>/<int:comment_pk>',views.comment_delete, name='comment_delete'),
    path('comment_update/<int:service_pk>/<int:comment_pk>',views.comment_update, name='comment_update'),
]
