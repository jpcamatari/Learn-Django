from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return HttpResponse('Faça seu Cadastro')

def auth(request):
    return HttpResponse('Você Está na autenticação')
