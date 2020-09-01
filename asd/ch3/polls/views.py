from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse

from django.template import loader
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]   # 날짜 기준 오름차순, 5개의 최근 Question 객체를 저장
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context) # 템플릿 이름 지정, 보낼 내용(선택) 지정
# Leave the rest of the views (detail, results, vote) unchanged


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
