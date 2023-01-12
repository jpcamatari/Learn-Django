from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro),
    path('valida_formulario', views.valida_formulario),
]