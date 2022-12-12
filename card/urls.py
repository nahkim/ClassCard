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

    # 카드 카테고리 검색을 한 후에 나타나는 카드 목록 페이지
    path('card_list/', views.card_list, name="card_list"),

    # 카드를 비교하기 위해서 비교하기 바구니에 넣고 / 비교하기 페이지
    path('bookmark/<int:pk>/', views.bookmark, name="bookmark"),
    path('card_compare/', views.card_compare, name="card_compare"),

    # 카드를 검색했을 떄 보이는 카드 목록 페이지
    path('search/card_list/', views.search_list, name="search_list"),
    path('rank/',views.rank, name='rank'),
]