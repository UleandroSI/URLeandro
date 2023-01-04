from django import forms
from saveurl.models import Cadastro


class CadastroForms(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = '__all__'
        labels = {"enviar": "Enviar link para seu email"}