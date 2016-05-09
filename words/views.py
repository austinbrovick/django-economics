from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import WordForm
from .models import Word


def word_list(request):
    return render(request, 'words/words_list.html', {'words':Word.objects.all()})


class WordCreate(View):
    template_name = 'words/words_create.html'
    form = WordForm


    def get(self, request):
        return render(request, self.template_name, {'form':self.form()})
    def post(self, request):
        word = self.form(request.POST)
        if word.is_valid():
            word.save()
            return redirect('words_list')
        else:
            return render(request, self.template_name, {'form':form})



def word_detail(request, pk):
    word = Word.objects.get(pk=pk)
    return render(request, 'words/word_detail.html', {'word':word})
