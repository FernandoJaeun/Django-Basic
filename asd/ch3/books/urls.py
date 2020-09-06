from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.BooksModelView.as_view(), name='indes'),

    path('book/', views.BookList.as_view(), name='book_list'),

    path('author/', views.AuthorList.as_view(), name = 'author_list'),

    path('publisher/', views.publisher.as_view(), name = 'publisher_list'),

    path('book/<int:pk>/', views.BookDetail.as_view(), name = 'book_detail'),

    path('author/<int:pk>/', views.AuthorDetail.as_view(), name = 'author_detail'),

    path('publisher/<int:pk>', views.PublisherDetail.as_view(), name = 'publisher_detail'),
]
# 각 URL의 호출 인자를 as_view()로 정의한 것은 클래스형 뷰이기 때문이다