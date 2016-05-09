from django.conf.urls import url

from .views import equation_list

urlpatterns = [
    url(r'^$', equation_list, name='equations_list'),
]
