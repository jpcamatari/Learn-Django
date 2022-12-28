from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return render(request, 'index.html')

def auth(request):
    return HttpResponse('Você Está na autenticação')
