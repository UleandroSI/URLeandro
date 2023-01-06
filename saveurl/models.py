from django.db import models


# Create your models here.
class Cadastro(models.Model):
    """Uma típica classe definindo um modelo, derivada da classe Model."""
    # Campos
    nome = models.CharField(max_length=64, verbose_name='Nome', primary_key=True, name='nome', help_text='Endereço único da página, criado por Hash MD5.')
    created = models.DateField(name='created', auto_now_add=True, editable=False, help_text='Data de criação da página.')

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

class Envio(Cadastro):
    email = models.EmailField(blank=True, null=True, verbose_name='Email', name='email')
    enviar = models.BooleanField(default=False)