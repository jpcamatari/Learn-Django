from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('listar/', views.listar, name = 'listar'),
    path('listar/', views.listar_unico, name='listar_unico')
]