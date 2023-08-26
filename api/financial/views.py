from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from utils.proposal_valuation_service import ProposalValuation

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

    @action(detail=False, methods=['POST'])
    def make_proposal(self, request):
        data = request.data
        proposal_response = bool
        proposal_response = ProposalValuation().check_proposal(data)
        # if proposal_response:

        return Response(proposal_response, status=200)
