# URLeandro
## Django SaveURL


<p align="center">Um site alvar URL importantes para pesquisas. E te-las disponíveis e compartilhada online. 
Cria uma página de endereço único para salvar URLs importantes para serem visualizadas depois.
Links para serem utilizados em projetos, ou trabalhos, ou TCC.
A página é aberta para qualquer um que tenha o link, e pode ser compartilhada em grupos para contribuição.
</p>

<p align="center">
<a href="#about">Sobre</a> .
<a href="#tecnologias">Tecnologias</a> .
<a href="#requesites">Pré Requesitos</a> .
<a href="#licence">Licença</a> .
<a href="#autor">Autor</a> .
</p>
 
<br>

<h4 align="center">
	🚧Projeto SaveURL	🚀 Em contrução... 🚧
</h4>
### O que faz o projeto

- [] Criar descrição do Projeto.
- [] Criar backend com Python.
- [] Criar template para páginas de Django.
- [] GIF's de demonstração de funcionamento.
	
### Tecnologias
- [Python 3]()
- [Django 10]()
- [HTML]()
- [BootStrap 5]()
- [MySQL](https://dev.mysql.com/doc/)

#requesites
### Pré Requesitos
Antes de começar é necessário ter instalado as seguintes ferramentas:

```bash
# Python 3
$ git clone <https://github.com/uleandrosi/URLeandro

# Va na pasta do projeto
$ cd projeto

# Instale as depedências
$ yarn

# Execute a aplicação
$ yarn start
```


### Problemas
- Ao acessar a página apresenta formulário:
```
<form action="{% url 'index' %}" name="cadastro" method="POST" novalidate>
<input type="text" class="form-control" id="nome" placeholder="Nome para Link" name="nome" size="40" value="{{ nome }}">
<button type="submit" class="btn btn-primary">Submit</button>
</form>
```
- Então gera um hashSHA256, que será o field=nome na tabela Cadastros do Models, que será o ID e URL para acesso à página.
```
nome = models.CharField(max_length=64, verbose_name='Nome', primary_key=True, name='nome', help_text='Endereço único da página, criado por Hash MD5.')
```
- Ao criar já é direcionado para a página com outro formulário para inserir os links:
```
<form action="{% url 'dados' %}" name="inserir" method="POST">
<input type="text" class="form-control" id="input_url" placeholder="Insira a URL aqui." name="input_url">
<button type="submit" class="btn btn-primary">Submit</button>
</form>
```
- Nesta página unica será inserido os links para cada página do site atrelado ao ID que é a própria URL.

- Estou com dificuldades para montar as views.


*** 
### Autor
By uLeandroSP [See my Github](https://github.com/UleandroSI)
***
### Referências
[Bootstrap](https://www.bootstrapcdn.com)

[Django W3Schools](https://www.w3schools.com/django/index.php)

[Django Crispy](https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs)

[Django CheckBox](https://stackoverflow.com/questions/42768057/django-checkbox-field)

[Django Samuel Gonçalves](https://www.youtube.com/watch?v=4OHyK_l75ic&list=PLjzlTD1oGVYLHFrIwY23V5blOCHtFpIVD&index=12)

[Formulários](https://www.youtube.com/watch?v=rzyoT2ZDy1c)

[Model Form](https://vinaykumarmaurya30.medium.com/saving-data-using-django-model-form-7ec9d8471ccf)

[Django Mozilla](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Tutorial_local_library_website)

[Django Básico](https://www.youtube.com/watch?v=hPJkM9C5FSA&list=PLHWfNMxB2F4HdKbo8zdgXyxVDOxH429Ko&index=13)

[Django Models Custon](https://pythonacademy.com.br/blog/formularios-do-django-com-django-forms)

[Python Guides Django](https://pythonguides.com/django/)

