from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Usuario

def cadastro(request):
    if request.method == "GET":
        return render(request, 'index.html')

    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario = Usuario(nome = nome,
                          email = email,
                          senha = senha)

        usuario.save()

def listar(request):
    usuarios = Usuario.objects.all().exclude(name = joao)
    return render(request, "listar.html", {'usuarios' : usuarios})
