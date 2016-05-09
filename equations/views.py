from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import WordForm
from .models import Word



def word_list(request):
    words = Word.objects.all()
    return render(request, 'equations/equations_list.html')

