from django.shortcuts import render, get_list_or_404
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
   usuarios = Usuario.objects.all()
   return render(request, "listar/listar.html", {'usuarios' : usuarios})


def listar_unico(request, id):
    usuario = get_list_or_404(Usuario, id = id)
    return render(request, 'listar/listar.html', {'usuarios': usuario})

