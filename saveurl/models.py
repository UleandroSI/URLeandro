from django.db import models


# Create your models here.
class Cadastro(models.Model):
    """Uma típica classe definindo um modelo, derivada da classe Model."""
    # Campos
    nome = models.CharField(max_length=64, verbose_name='Nome', primary_key=True, name='nome', help_text='Endereço único da página, criado por Hash MD5.')
    created = models.DateField(auto_now_add=True, name='created', editable=False, help_text='Data de criação da página.')

    # Metadados
    class Meta:
        ordering = ['-created']
        verbose_name = 'Paginas'

    # Métodos
    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de Cadastro."""
        return reversed('model-detail-view', args=[str(self.nome)])

    def __str__(self):
        """ String para representar o objeto Cadastro (no site Admin)."""
        return self.nome


class Dados(models.Model):
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE, null=True)
    urls = models.URLField(max_length=400, verbose_name='urls', name='urls', help_text='URLs para armazenar.')
    created = models.DateField(auto_now_add=True, name='created', editable=False, help_text='Data que o link foi inserido.')
    updated = models.DateField(auto_now=True, name='updated', editable=False, help_text='Data da ultima atualização da página.')

    class Meta:
        ordering = ['-updated']
        verbose_name = 'Dados'

    def __str__(self):
        # String para representar o objeto Cadastro (no site Admin).
        return self.urls

    # Métodos
    def get_absolute_url(self):
        # Retorna a url para acessar uma instancia específica de Cadastro.
        return reversed('model-detail-view', args=[str(self.cadastro)])