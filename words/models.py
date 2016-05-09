from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

ECONOMICS = (
    ('microeconomics', 'MICROECONOMICS'),
    ('macroeconomics', 'MACROECONOMICS'),
    ('both', 'BOTH')
)



class Word(models.Model):
    econ = models.CharField('economics class', max_length=30, choices=ECONOMICS)
    word = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['word']

    def __unicode__(self):
        return self.word



    def get_absolute_url(self):
        return reverse('words_word_detail', kwargs={'pk':self.pk})



class Definition(models.Model):
    definition = models.TextField()
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return "{} - {}".format(self.word, self.definition)


    class Meta:
        verbose_name = 'definition'
        ordering = ['-votes']


    def get_word_url(self):
        word = self.word
        return word.get_absolute_url()


    def check_votes(self):
        if self.votes < -3:
            self.delete()




