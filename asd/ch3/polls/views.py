from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import URLResolver,  reverse   # url 처리를 위한 reverse 
from django.template import loader

from django.views import generic # 클래스형 뷰 제네릭 호출~
from .models import Choice, Question


#--- Class-Based GenericView
class IndexView(generic.ListView):
    template_name = 'polls/index.html' # 템플릿 파일명 지정
    context_object_name = 'latest_question_list'    
    def get_queryset(self): 
        "최근 생성된 질문 5개를 반환함"
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



# def index(request):
#     latest_question_list = Question.objects.order_by(
#         'pub_date')[:5]   # 날짜 기준 오름차순, 5개의 최근 Question 객체를 저장
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # 템플릿 이름 지정, 보낼 내용(선택) 지정
#     return render(request, 'polls/index.html', context)
# # Leave the rest of the views (detail, results, vote) unchanged


# def detail(request, question_id):
#     # 두번째 인자 조건이 성립하지 않으면 Http404 익셉션 발생
#     question = get_object_or_404(Question, pk=question_id)    # 단축함수 : ShortCut
#     return render(request, 'polls/detail.html', {'question': question})
#     # render(request : 응답을 받아야 이 함수가 생성되고, 사용된다.
#     #        template_name : request와 함께 필수 파라미터. 화면에 내용을 뿌려야하니까 뿌릴 화면을 지정해줘야지?
#     #        context : 딕셔너리형,  디폴트는 빈 딕셔너리. 템플릿의 내용이 될 녀석이다)


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)    # 단축함수 : ShortCut
#     return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # Question 모델에서 question_id 인덱스에 해당하는 값이 있으면 반환하고, 없으면 404 에러를 반환
    try:
        selected_chocie = question.choice_set.get(pk=request.POST['choice'])    
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didin't select a choice"
        })
    else:
        selected_chocie.votes += 1
        selected_chocie.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
