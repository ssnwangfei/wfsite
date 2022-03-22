from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'name': 'The World',
        'message': 'hello',
    }
    return render(request, 'main\index.html', context)
