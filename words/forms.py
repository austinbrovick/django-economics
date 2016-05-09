from django import forms

from .models import Word


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['econ', 'word']

    def save(self):
        word = Word.objects.create(word=self.cleaned_data['word'], econ=self.cleaned_data['econ'])



