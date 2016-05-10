from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from .forms import WordForm, DefinitionForm
from .models import Word, Definition


def word_list(request):
    all_words = Word.objects.all()
    words_with_dict = {}
    words = []
    for word in all_words:
        print(word.definition_set.count())
        words.append({'word':word, 'defs': word.definition_set.count()})
    return render(request, 'words/words_list.html', {'words': words})

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
            return render(request, self.template_name, {'form':self.form()})

def word_detail(request, pk):
    word = Word.objects.get(pk=pk)
    definitions = Definition.objects.filter(word=word)
    context = {'word':word, 'form':DefinitionForm(), 'definitions': definitions}
    return render(request, 'words/word_detail.html', context)


class DefinitionCreate(View):
    form = DefinitionForm
    def get(self, request, pk):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        word = Word.objects.get(pk=pk)
        return redirect(word.get_absolute_url())

    def post(self, request, pk):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        definition = self.form(request.POST)
        word = Word.objects.get(pk=pk)
        if definition.is_valid():
            instance = definition.save(commit=False)
            instance.word = word
            instance.save()
        return redirect(word.get_absolute_url())

class DefinitionDownVote(View):
    def get(self, request, pk):
        definition = Definition.objects.get(pk=pk)
        url = definition.get_word_url()
        definition.votes -= 1
        definition.save()
        definition.check_votes()
        return redirect(url)



class DefinitionUpVote(View):
    def get(self, request, pk):
        definition = Definition.objects.get(pk=pk)
        definition.votes += 1
        definition.save()
        return redirect(definition.get_word_url())

def words_micro(request):
    all_words = Word.objects.filter(econ='microeconomics')
    words_with_dict = {}
    words = []
    for word in all_words:
        print(word.definition_set.count())
        words.append({'word':word, 'defs': word.definition_set.count()})
    return render(request, 'words/micro_list.html', {'words': words})

def words_macro(request):
    all_words = Word.objects.filter(econ='macroeconomics')
    words_with_dict = {}
    words = []
    for word in all_words:
        print(word.definition_set.count())
        words.append({'word':word, 'defs': word.definition_set.count()})
    return render(request, 'words/macro_list.html', {'words': words})


def words_both(request):
    all_words = Word.objects.filter(econ='both')
    words_with_dict = {}
    words = []
    for word in all_words:
        print(word.definition_set.count())
        words.append({'word':word, 'defs': word.definition_set.count()})
    return render(request, 'words/both_list.html', {'words': words})

