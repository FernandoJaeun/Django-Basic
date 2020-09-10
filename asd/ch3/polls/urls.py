from django.urls import path
from . import views

app_name = 'polls'  # url의 이름이 같아도 app_name을 보고 구분한다
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),    #/polls/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), #/polls/5
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'), #/polls/5/result
    path('<int:question_id>/vote/', views.vote, name='vote'), #/polls/5/vote
    # /admin/  기본 제공

]