from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from student.models import Question


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    # full :
    template = loader.get_template('student/index.html')
    context = {'questions': latest_questions}
    return HttpResponse(template.render(context, request))
    # shortcut:
    # return render(request, 'student/index.html', {'questions': latest_questions})


# Create your views here.
def detail(request, question_id):
    # # full:
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("This question does not exist")

    # shortcut:
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'student/detail.html', {'question': question})


def results(request, question_id):
    response = 'You are looking at the results of question %s'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
