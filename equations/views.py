from django.shortcuts import render, redirect
from django.views.generic import View




def equation_list(request):
    return render(request, 'equations/equations_list.html')
