from django.shortcuts import render
from django.http import HttpResponse
import json

def cadastro(request):
    return render(request, 'index.html')

def valida_formulario(request):
    nome = request.GET.get('nome')
    email = request.GET.get('email')
    return HttpResponse(json.dumps({'nome': nome, 'email': email}))
    