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
