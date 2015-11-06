from django.conf.urls import url

from . import views

urlpatterns = [
    # index
    url(r'^$', views.index, name='index'),
    # polls/id -> polls/3
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='dettagli'),
    # polls/id/risultati
    url(r'^(?P<question_id>[0-9]+)/risultati/$', views.results, name='risultati'),
    # polls/id/voti
    url(r'^(?P<question_id>[0-9]+)/vota/$', views.vote, name='vota'),
]
