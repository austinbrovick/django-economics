from django.conf.urls import url

from .views import word_list, WordCreate, word_detail, DefinitionCreate, DefinitionDownVote, DefinitionUpVote, words_micro, words_macro, words_both

urlpatterns = [
    url(r'^$', word_list, name='words_list'),
    url(r'^create/$', WordCreate.as_view(), name='words_word_create'),
    url(r'^(?P<pk>\d+)/$', word_detail, name='words_word_detail'),
    url(r'^create/(?P<pk>\d+)/$', DefinitionCreate.as_view(), name='words_definition_create'),


    url(r'^upvote/(?P<pk>\d+)/$', DefinitionUpVote.as_view(), name='words_definition_upvote'),
    url(r'^downvote/(?P<pk>\d+)/$', DefinitionDownVote.as_view(), name='words_definition_downvote'),

    url(r'^microeconomics/$', words_micro, name='words_micro'),
    url(r'^macroeconomics/$', words_macro, name='words_macro'),
    url(r'^micro_and_macro/$', words_both, name='words_both'),

]
