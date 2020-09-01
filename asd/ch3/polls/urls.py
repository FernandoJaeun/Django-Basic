from django.urls import path
from . import views

app_name = 'polls'  # url의 이름이 같아도 app_name을 보고 구분한다
urlpatterns = [
    path('', views.index, name='index'),    #/polls/
    path('<int:question_id>/', views.detail, name='detail'), #/polls/5
    path('<int:question_id>/results/', views.results, name='results'), #/polls/5/result
    path('<int:question_id>/vote/', views.vote, name='vote'), #/polls/5/vote
    # /admin/  기본 제공

]