from django.db import models


class BookModel(models.Model):
    class ReadStatus(models.IntegerChoices):
        TO_READ = 1, 'Quero Ler'
        READING_NOW = 2, 'Lendo Agora'
        WAS_READ = 3, 'Foi Lido'

    author = models.CharField(max_length=200, verbose_name='Autor')
    title = models.CharField(max_length=200, verbose_name='Título do livro')
    description = models.TextField(blank=True, verbose_name='Descrição do livro')
    published = models.PositiveSmallIntegerField(default=0, verbose_name='Ano de publicação')
    read_status = models.PositiveSmallIntegerField(
        verbose_name='Status da leitura',
        choices=ReadStatus.choices,
        default=ReadStatus.TO_READ,
    )
