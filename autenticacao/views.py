from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Usuario, Cargos

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
    if len(request.GET) != 0:
        nome = request.GET.get('nome')
        email = request.GET.get('email')
        senha = request.GET.get('senha')

        cargo = Cargos.objects.get(id=1)

        pessoa = Usuario(nome = nome,
                         email = email,
                         senha = senha,
                         cargo = cargo)
        pessoa.save()


    usuarios = Usuario.objects.all()
    return render(request, "listar.html", {'usuarios' : usuarios})
