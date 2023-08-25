from django.db import models


class LoggedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='criado em')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='atualizado em')

    class Meta:
        abstract = True
