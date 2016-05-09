from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import WordForm, DefinitionForm
from .models import Word, Definition


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
    return render(request, 'words/word_detail.html', {'word':word, 'form':DefinitionForm()})


class DefinitionCreate(View):
    form = DefinitionForm
    def get(self, request, pk):
        pass

    def post(self, request, pk):
        definition = self.form(request.POST)
        if definition.is_valid():
            word = Word.objects.get(pk=pk)
            instance = definition.save(commit=False)
            instance.word = word
            instance.save()
        return redirect(word.get_absolute_url())





