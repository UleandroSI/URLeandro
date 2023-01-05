from django.shortcuts import render, HttpResponse, redirect
from .forms import CadastroForms
from saveurl.models import Cadastro
import hashlib, time


# Create your views here.
def index(request):
    formulario = CadastroForms()
    if request.method == 'GET':
        dados = Cadastro.objects.all()

        context = {
            'dados': dados,
            'form': formulario,
        }

        return render(request, 'saveurl/index.html', context)

    elif request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            data = time.time()
            nome = str(form['nome']).encode()
            data = str(data).encode()
            hash = hashlib.sha1(nome + data)
            form['nome'] = hash.hexdigest()
            form.save()
            return redirect("/")
        else:
            dados = Cadastro.objects.all()
            context = {
                'dados': dados,
                'form': formulario,
            }

            return render(request, 'saveurl/index.html', context)
