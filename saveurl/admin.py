from django.contrib import admin
from .models import Cadastro, Dados


# Register your models here.
class CadastroAdmin(admin.ModelAdmin):
    list_display = ("created", "nome")
    list_filter = ("created", "nome")
    search_fields = ["nome"]

admin.site.register(Cadastro, CadastroAdmin)


class DadosAdmin(admin.ModelAdmin):
    list_display = ('cadastro', 'urls', 'created', 'updated')
    list_filter = ('updated', 'created')
    search_fields = ['urls']

admin.site.register(Dados, DadosAdmin)