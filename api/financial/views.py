from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from financial.tasks import check_proposal_availability
from financial.serializers import (
    ProposalStatusSerializer, ProposalFieldsSerializer, FinancialProposalSerializer, FinancialProposalForm)
from financial.models import ProposalStatus, ProposalFields, FinancialProposal


class ProposalStatusView(viewsets.ReadOnlyModelViewSet):
    queryset = ProposalStatus.objects.all()
    serializer_class = ProposalStatusSerializer


class ProposalFieldsView(viewsets.ReadOnlyModelViewSet):
    queryset = ProposalFields.objects.filter(enabled=True)
    serializer_class = ProposalFieldsSerializer


class FinancialProposalView(viewsets.ModelViewSet):
    queryset = FinancialProposal.objects.all().order_by('-id')

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return FinancialProposalForm
        return FinancialProposalSerializer

    @action(detail=False, methods=['POST'])
    def make_proposal(self, request):
        check_proposal_availability.delay(request.data)
        return Response({'msg': 'A proposta foi enviada para o analisador, e ficará disponível em alguns momentos.'}, status=201)
