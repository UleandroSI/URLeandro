from django import forms
from saveurl.models import Cadastro, Dados


class CadastroForms(forms.ModelForm):

    email = forms.EmailField(
        label='Email',
        required=False,
    )
    enviar = forms.BooleanField(
        label='Enviar por e-mail',
        required=False,
    )
    class Meta:
        model = Cadastro
        fields = ['nome']
        # Campos que não estarão no form
        exclude = ['created']


class DadosForms(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ['urls']
        exclude = ['cadastro', 'created', 'updated']