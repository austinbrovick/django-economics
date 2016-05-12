from django.forms import ModelForm, Textarea

from .models import Word, Definition


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['econ', 'word']

    # def save(self):
    #     word = Word.objects.create(word=self.cleaned_data['word'], econ=self.cleaned_data['econ'])


class DefinitionForm(ModelForm):
    class Meta:
        model = Definition
        fields = ['definition']
        widgets = {
            'definition':Textarea(attrs={'rows':3, 'class':'form-control'})
        }


