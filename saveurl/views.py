from django.shortcuts import render
from .forms import CadastroForms


# Create your views here.
def index(request):
    if request.method == 'GET':
        form = CadastroForms()
        return render(request, 'saveurl/index.html', {'form': form})