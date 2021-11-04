from django import template
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views.generic import *
from .models import Choice, Question
from polls import models

# Create your views here.
def index(req):
    latest_question_list =  Question.objects.order_by('-pub_date')
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    return HttpResponse(template.render(context, req))


def detail(request, question_id):
    try: 
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html" , { "question": question }) 




class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', { 
                "question": question,
                "error_message": "You didn't selected any choice"
            })

    choice.votes += 1
    choice.save()

    return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))



