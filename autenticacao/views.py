from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    nome = 'João Paulo'
    idade = 28
    profissao = 'Programador'

    return render(request, 'index.html', {'nome': nome, 'idade':idade, 'profissão':profissao})

def auth(request):
    return HttpResponse('Você Está na autenticação')
