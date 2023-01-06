from django.shortcuts import render, HttpResponse, redirect
from .forms import CadastroForms, EnvioForms
from saveurl.models import Cadastro, Envio
import hashlib, time


# Create your views here.
def index(request):
    #formulario = CadastroForms()
    form = CadastroForms()
    if request.method == 'GET':
        dados = Envio.objects.all()

        context = {
            'dados': dados,
            'form': form,
        }

        return render(request, 'saveurl/index.html', context)

    elif request.method == 'POST':
        form = CadastroForms(request.POST or None)

        if form.is_valid():
            data = time.time()
            nome = str(form['nome']).encode()
            data = str(data).encode()
            hash = hashlib.md5(nome + data)
            hashex = hash.hexdigest()
            form.save()
            return redirect("/")
        else:
            dados = Envio.objects.all()
            context = {
                'dados': dados,
                'form': form,
            }

            return render(request, 'saveurl/index.html', context)
