from django.contrib import admin
from .models import Cadastro, Dados


class CadastroAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "created")
    list_filter = ("nome", "id", "created")
    search_fields = ["nome"]

admin.site.register(Cadastro, CadastroAdmin)


class DadosAdmin(admin.ModelAdmin):
    list_display = ('cadastro_id', 'urls', 'created', 'updated')
    list_filter = ('updated', 'created')
    search_fields = ['urls']

admin.site.register(Dados, DadosAdmin)