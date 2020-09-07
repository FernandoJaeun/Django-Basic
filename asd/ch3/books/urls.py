from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    # /books/
    path('', views.BooksModelView.as_view(), name='indes'),

    # /books/book/
    path('book/', views.BookList.as_view(), name='book_list'),

    # /books/author/
    path('author/', views.AuthorList.as_view(), name = 'author_list'),

    # /books/publisher/
    path('publisher/', views.publisher.as_view(), name = 'publisher_list'),

    # /books/book/99/
    path('book/<int:pk>/', views.BookDetail.as_view(), name = 'book_detail'),

    # /books/author/99/
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name = 'author_detail'),

    # /books/publisher/99
    path('publisher/<int:pk>', views.PublisherDetail.as_view(), name = 'publisher_detail'),
]
# 각 URL의 호출 인자를 as_view()로 정의한 것은 클래스형 뷰이기 때문이다