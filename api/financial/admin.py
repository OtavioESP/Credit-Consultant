from django.contrib import admin

from financial.models import ProposalStatus, ProposalFields, FinancialProposal


@admin.register(ProposalStatus)
class ProposalStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(ProposalFields)
class ProposalFieldsAdmin(admin.ModelAdmin):
    pass


@admin.register(FinancialProposal)
class FinancialProposalAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'person', 'proposal_data']
