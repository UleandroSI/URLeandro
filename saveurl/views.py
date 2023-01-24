from django.shortcuts import render, redirect
from saveurl.models import Cadastro, Dados
from .forms import DadosForms
import hashlib, time
import re


def home(request):
    """View function for home page of site."""
    contexto = {}
    data_atual = time.time()
    salvar = Cadastro()
    nome = request.POST.get('nome', None)
    email = request.POST.get('email', None)
    enviar = request.POST.get('check_email', None)

    if request.method == 'POST':
        erros = {}

        """ Valida Nome"""
        if not nome:
            erros['nome'] = ("Digite um Nome para o link.")
        elif len(nome) > 40:
            erros['nome'] = ("Limite de 40 caracteres.")
        else:
            """ Valida email"""
            if not email:
                if not enviar:
                    pass
                else:
                    erros['email'] = ("Digite um email para enviar o link da sua página.")
            elif not emailRegex(email):
                erros['email'] = ("Digite um email para enviar o link da sua página.")
            elif not enviar:
                erros['enviar'] = ("Para receber o link por email, deve selecionar o Checkbox.")

        if erros:
            contexto['erros'] = erros
            contexto['nome'] = nome
            contexto['email'] = email
            contexto['enviar'] = enviar
        else:
            nome = nome.encode()
            data = str(data_atual).encode()
            hash = hashlib.sha256(nome + data)
            salvar.nome = hash.hexdigest()

            salvar.save()

            #contexto['mensagem'] = "Sua página foi criada com sucesso. Link: "
            #return render(request, 'saveurl/index.html', context=contexto)
            return render(request, list_dados, salvar.nome)

    else:
        contexto['nome'] = nome
        contexto['email'] = email
        contexto['enviar'] = enviar

    return render(request, 'saveurl/index.html', context=contexto)


def simples(request):
    pagina = Cadastro.objects.get(nome='nome')
    return render(request, 'saveurl/exemplo.html', {"nome":pagina})


def list_dados(request, url_parameter):
    context = {}
    cadastros = Cadastro.objects.get(nome=url_parameter)
    cadastro_id = cadastros.id
    print(cadastro_id)
    dados_id = Dados.objects.filter(cadastro_id=cadastro_id)
    print(dados_id)

    context['dados'] = dados_id
    context['url_parameter'] = url_parameter
    return render(request, 'saveurl/dados_list.html', context)


def emailRegex(s):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
      return True
   return False