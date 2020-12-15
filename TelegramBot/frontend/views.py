from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def page(request):
    return render(request, 'custom.html', {
        'videos': 'https://www.youtube.com'
    })


def index(request):
    return render(request, 'index.html', {
        'videos': 'https://www.youtube.com'
    })
