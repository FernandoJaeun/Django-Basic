from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import URLResolver, path, register_converter, reverse
from django.template import loader
from .models import Choice, Question



def index(request):
    latest_question_list = Question.objects.order_by(
        'pub_date')[:5]   # 날짜 기준 오름차순, 5개의 최근 Question 객체를 저장
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # 템플릿 이름 지정, 보낼 내용(선택) 지정
    return render(request, 'polls/index.html', context)
# Leave the rest of the views (detail, results, vote) unchanged


def detail(request, question_id):
    # 두번째 인자 조건이 성립하지 않으면 Http404 익셉션 발생
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_chocie = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didin't select a choice"
        })
    else:
        selected_chocie.votes += 1
        selected_chocie.sava()
