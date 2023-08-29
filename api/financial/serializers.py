from rest_framework import serializers

from financial.models import ProposalStatus, ProposalFields, FinancialProposal

from person.serializers import PersonSerializer


class ProposalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalStatus
        fields = ['id', 'name', 'description']


class ProposalFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalFields
        fields = [
            'id',
            'name',
            'description',
            'required',
            'enabled',
            'type',
        ]


class FinancialProposalSerializer(serializers.ModelSerializer):
    status = ProposalStatusSerializer()
    person = PersonSerializer()

    class Meta:
        model = FinancialProposal
        fields = ['id', 'status', 'person', 'proposal_data']


class FinancialProposalForm(serializers.ModelSerializer):
    class Meta:
        model = FinancialProposal
        fields = ['status', 'person', 'proposal_data']
