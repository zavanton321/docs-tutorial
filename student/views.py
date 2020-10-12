from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from student.models import Question, Choice


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'student/index.html', {'questions': latest_questions})


def detail(request, question_id):
    return render(request, 'student/detail.html', context={
        'question': get_object_or_404(Question, pk=question_id)
    })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'student/detail.html', context={
            'question': question,
            'error_message': "You haven't selected any choice!"
        })
    else:
        # race conditions here
        # selected_choice.votes += 1

        # avoid race condition (DB is responsible for updating the field)
        selected_choice.votes = F('votes') + 1
        selected_choice.save()

        # full version
        # return HttpResponseRedirect(reverse('student:results', kwargs={'question_id': question_id}))

        # short version
        return redirect(reverse('student:results', kwargs={'question_id': question_id}))


def results(request, question_id):
    return render(request, 'student/results.html', context={
        'question': get_object_or_404(Question, pk=question_id)
    })
