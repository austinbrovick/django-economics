from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View

from words.models import Word


# Create your views here.


class Search(View):
    def get(self, request):
        pass
    def post(self, request):
        search = request.POST.get('search')
        print(search)
        return HttpResponse("hello world")
