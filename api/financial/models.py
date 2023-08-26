from django.db import models

from utils.versioned_models import LoggedModel


class ProposalStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name='nome')
    description = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='descricao')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Status da proposta'


class ProposalFields(LoggedModel):
    INPUT_TYPES = [
        ('text', 'Text'),
        ('number', 'Number'),
    ]

    name = models.CharField(max_length=100, verbose_name='nome')
    description = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='descricao')
    required = models.BooleanField(
        default=False, verbose_name='obrigatorio', help_text='Marque para deixar o campo obrigatório')
    enabled = models.BooleanField(default=False, verbose_name='habilitado',
                                  help_text='marque para manter que o campo apareça no formulario de envio')
    type = models.CharField(
        max_length=50, choices=INPUT_TYPES, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Campo da proposta'
        verbose_name_plural = 'Campos da proposta'


class FinancialProposal(LoggedModel):
    status = models.ForeignKey(
        ProposalStatus, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = 'Proposta financeira'
        verbose_name_plural = 'Propostas financeiras'
