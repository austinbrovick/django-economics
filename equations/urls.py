from django.conf.urls import url

from .views import word_list

urlpatterns = [
    url(r'^$', word_list, name='equations_list'),
]
