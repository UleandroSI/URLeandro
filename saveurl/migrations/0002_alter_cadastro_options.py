# Generated by Django 4.1.5 on 2023-01-06 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saveurl', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadastro',
            options={'ordering': ['created'], 'verbose_name': 'Paginas'},
        ),
    ]