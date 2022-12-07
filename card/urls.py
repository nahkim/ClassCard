from django.urls import path
from . import views

app_name = 'card'

urlpatterns = [
    path('detail/<int:num>/', views.detail, name="detail"),
    path('search/',views.search, name='search'),
    path('comment/<int:pk>/', views.comment, name="comment"),
    path('comment_delete/<int:card_id>/<int:comment_pk>/', views.comment_delete, name="comment_delete"),
    path('comment_update/<int:card_id>/<int:comment_pk>/', views.comment_update, name="comment_update"),
    path('cardcompany/',views.cardcompany,name='cardcompany'),
]