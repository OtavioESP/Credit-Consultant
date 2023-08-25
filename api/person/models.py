from django.db import models

from utils.versioned_models import LoggedModel

# Create your models here.


class Person(LoggedModel):
    full_name = models.CharField(max_length=200, verbose_name='nome completo')
    email = models.EmailField(max_length=100)
    adress = models.TextField(max_length=500, verbose_name='endereco')
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Pessoa Fisica'
        verbose_name_plural = 'Pessoas Fisicas'

    def __str__(self):
        return f'{self.cpf}'
