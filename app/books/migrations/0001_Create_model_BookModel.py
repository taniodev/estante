# Generated by Django 3.2.3 on 2021-07-14 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, verbose_name='Autor')),
                ('title', models.CharField(max_length=200, verbose_name='Título do livro')),
                ('description', models.TextField(blank=True, verbose_name='Descrição do livro')),
                ('published', models.PositiveSmallIntegerField(default=0, verbose_name='Ano de publicação')),
                ('read_status', models.PositiveSmallIntegerField(choices=[(1, 'Quero Ler'), (2, 'Lendo Agora'), (3, 'Foi Lido')], default=1, verbose_name='Status da leitura')),
            ],
        ),
    ]
