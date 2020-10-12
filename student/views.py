from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from student.models import Question, Choice


class IndexView(ListView):
    template_name = 'student/index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailedView(DetailView):
    model = Question
    template_name = 'student/detail.html'
    context_object_name = 'question'


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'student/detail.html', context={
            'question': question,
            'error_message': "You haven't selected any choice!"
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return redirect(reverse('student:results', kwargs={'pk': pk}))


class ResultsView(DetailView):
    model = Question
    template_name = 'student/results.html'
    context_object_name = 'question'
