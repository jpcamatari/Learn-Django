from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    pessoa = {'nome': 'João Paulo', 'idade': 28, 'profissao': 'Programador'}

    return render(request, 'index.html')

