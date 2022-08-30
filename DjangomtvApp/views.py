from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {'Lista': 'Familiar'}
    return render(request, 'fliar_list.html', context)


