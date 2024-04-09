from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404

from .models import Question


# Create your views here.


def index(request):
    return render(request, "quiz/index.html")


def detail(request, question_number):
    question = get_object_or_404(Question, pk=question_number)
    return render(request, "quiz/detail.html", {"question": question})
