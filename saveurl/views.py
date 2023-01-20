from django.shortcuts import render, HttpResponse, redirect
from saveurl.models import Cadastro, Dados
from .forms import DadosForms
from django.views.generic import ListView
import hashlib, time
import re

# Create your views here.
def home(request):
    pagina = Cadastro.objects.get(nome='nome')
    return render(request, 'saveurl/exemplo.html', {"nome":pagina})


def lista(request):
    pagina = Cadastro.objects.get(nome='nome')
    return render(request, 'saveurl/exemplo.html', {"nome": pagina})

def emailRegex(s):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
      return True
   return False