from django.contrib import admin
from django.urls import path, include
from index import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacao/', include('autenticacao.urls')),
    path('', views.index),
]
