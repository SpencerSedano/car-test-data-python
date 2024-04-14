from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404

from .models import Question

import random

# Create your views here.


def index(request):
    list_questions = Question.objects.all()
    context = {"list_questions": list_questions}
    return render(request, "quiz/index.html", context)


def detail(request, question_number):
    question = get_object_or_404(Question, pk=question_number)
    context = {"question": question}
    return render(request, "quiz/detail.html", context)


def exam(request):
    random_number_range = random.randrange(0, len(Question.objects.all()))
    list_number = Question.objects.get(question_number=random_number_range)
    context = {"list_number": list_number}
    return render(request, "quiz/exam.html", context)
