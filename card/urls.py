from django.urls import path
from . import views

app_name = 'card'

urlpatterns = [
    path('detail/<int:num>/', views.detail, name="detail"),
    path('search/',views.search, name='search'),
    path('comment/<int:pk>/', views.comment, name="comment"),
    path('comment_delete/<int:card_id>/<int:comment_pk>/', views.comment_delete, name="comment_delete"),
    path('comment_update/<int:card_id>/<int:comment_pk>/', views.comment_update, name="comment_update"),
    path('cardcompanylist/',views.cardcompanylist,name='cardcompanylist'),
    path('cardcompany/<str:company>/',views.cardcompany,name='cardcompany'),
    path('card_list/', views.card_list, name="card_list"),
    path('card_compare/', views.card_compare, name="card_compare"),
    path('search/card_list/', views.search_list, name="search_list"),
]