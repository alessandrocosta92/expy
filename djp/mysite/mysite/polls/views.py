from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404

from .models import Question

def index(request):
    # Inventiamo
    # Ordinamento ASC/DESC SQL a seconda del parametro get 'ord'
    # e re-inviato a dettagli.html come 'ordinamento'
    ord = request.GET.get('ord')
    query = 'pub_date'
    if ord == "asc":
        query = "-pub_date"
    latest_question_list = Question.objects.order_by(query)[:5]
    parametri = {
        'latest_question_list': latest_question_list,
        'ordinamento': ord
    }
    return render(request, 'polls/index.html', parametri)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # Creazione indici domanda precedente/successiva
    prec = int(question_id) - 1;
    succ = int(question_id) + 1;

    if not Question.objects.filter(pk=prec).exists():
        prec = None

    if not Question.objects.filter(pk=succ).exists():
        succ = None

    parametri = {
        'question': question,
        'prec': prec, # precedente
        'succ': succ, # Successivo
    }
    return render(request, 'polls/dettagli.html', parametri)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
