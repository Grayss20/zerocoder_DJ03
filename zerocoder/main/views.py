from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'caption': 'Ferrets Django'})


def new(request):
    return render(request, 'main/new.html')


def feeding(request):
    return render(request, 'main/feeding.html')


def play(request):
    return render(request, 'main/play.html')
