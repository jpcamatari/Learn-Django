from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacao/', include('autenticacao.urls')),
    path('auth/', include('login.urls')),
    path("", lambda request: redirect('auth/login/'))

]
