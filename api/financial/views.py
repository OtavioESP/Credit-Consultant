from rest_framework import viewsets

from financial.serializers import (
    ProposalStatusSerializer, ProposalFieldsSerializer, FinancialProposalSerializer, FinancialProposalForm)
from financial.models import ProposalStatus, ProposalFields, FinancialProposal


class ProposalStatusView(viewsets.ReadOnlyModelViewSet):
    queryset = ProposalStatus.objects.all()
    serializer_class = ProposalStatusSerializer


class ProposalFieldsView(viewsets.ReadOnlyModelViewSet):
    queryset = ProposalFields.objects.all()
    serializer_class = ProposalFieldsSerializer


class FinancialProposalView(viewsets.ModelViewSet):
    queryset = FinancialProposal.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return FinancialProposalForm
        return FinancialProposalSerializer
