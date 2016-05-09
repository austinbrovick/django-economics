from django.conf.urls import url

from .views import word_list, WordCreate, word_detail

urlpatterns = [
    url(r'^$', word_list, name='words_list'),
    url(r'^create/$', WordCreate.as_view(), name='words_word_create'),
    url(r'^(?P<pk>\d+)/$', word_detail, name='words_word_detail'),
]
