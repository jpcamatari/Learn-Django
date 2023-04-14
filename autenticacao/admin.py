from django.contrib import admin
from .models import Usuario, Cargos

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'senha')
    readonly_fields = ('senha',)

admin.site.register(Cargos)

