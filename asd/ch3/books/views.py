from django.shortcuts import render

# 클래스형 제네릭 뷰를 사용하기 위함
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

# 테이블 조회를 위해 모델 클래스 가져옴
from .models import Book, Author, Publisher


# ---TemplateView
# books 어플리케이션의 첫 화면을 보여주는 구간

class BooksModelView(TemplateView):
    template_name = 'books/index.html'  # 클래스 변수를  overriding해서 필수 지정

    # 템플릿 시스템으로 넘겨줄 context 변수가 있는 경우 이 메스드를 overriding
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    # super(). __ 부모꺼 상속
        context['model_list'] = ['Book', 'Author',
                                 'Publisher']  # 첫 화면에 테이블 리스트를 보여주기 위해
        return context  # 얘도 필수


# ---ListView
class BookList(ListView):
    model = Book
    # default 템플릿 파일 = books/book_list.html


class AuthorList(ListView):
    model = Author
    # default 템플릿 파일 = books/author_list.html


class PublisherList(ListView):
    model = Publisher
    # default 템플릿 파일 = books/publisher_list.html


# ---DetailView
class BookDetail(DetailView):
    model = Book
    # default 템플릿 파일 = books/publisher_detail.html

class AuthorDetail(DetailView):
    model = Author
    # default 템플릿 파일 = books/publisher_detail.html

class PublisherDetail(DetailView):
    model = Publisher
    # default 템플릿 파일 = books/publisher_detail.html