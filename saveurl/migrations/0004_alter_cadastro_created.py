# Generated by Django 4.1.5 on 2023-01-07 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saveurl', '0003_alter_cadastro_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='created',
            field=models.DateField(editable=False, help_text='Data de criação da página.'),
        ),
    ]
