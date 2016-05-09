from __future__ import unicode_literals

from django.db import models

from words.models import Word



class Definition(models.Model):
    definition = models.TextField()
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    votes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return "{} - {}".format(self.word, self.definition)


    class Meta:
        verbose_name = 'definition'
        ordering = ['votes']
