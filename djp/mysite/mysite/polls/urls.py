from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

# routing url

# Browser richiede pagina, il routing url la trova (regexp) (oppure 404)
# models.py (modello) definisce gli oggetti e la relazione col database
# la view riceve richieste dal routing e invia altre richieste, templetizzate o meno
# (vedere index e details templetizzati), passando eventuali parametri (in index gestisco un get di ordinamento)
