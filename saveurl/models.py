from django.db import models


# Create your models here.
class Cadastro(models.Model):
    """Uma típica classe definindo um modelo, derivada da classe Model."""
    ENVIAR_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    # Campos
    nome = models.CharField(max_length=64, verbose_name='Nome', primary_key=True, name='nome', help_text='Endereço único da página, criado por Hash MD5.')
    email = models.EmailField(blank=True, null=True, verbose_name='Email', name='email')
    enviar = models.BooleanField(default=False)
    created = models.DateField(name='created', auto_now_add=True, help_text='Data de criação da página.')

    # Metadados
    class Meta:
        ordering = ['-nome']
        verbose_name = 'Cadastros'

    # Métodos
    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de Cadastro."""
        return reversed('model-detail-view', args=[str(self.nome)])

    def __str__(self):
        """ String para representar o objeto Cadastro (no site Admin)."""
        return self.nome

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None, *args, **kwargs
    ):
        super(Cadastro, self).save()