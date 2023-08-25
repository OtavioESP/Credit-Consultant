from rest_framework import serializers

from financial.models import ProposalStatus, ProposalFields, FinancialProposal


class ProposalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalStatus
        fields = ['id', 'name', 'description']


class ProposalFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalFields
        fields = [
            'name',
            'description',
            'required',
            'enabled'
        ]


class FinancialProposalSerializer(serializers.ModelSerializer):
    status = ProposalStatusSerializer()

    class Meta:
        model = FinancialProposal
        fields = ['id', 'status']


class FinancialProposalForm(serializers.ModelSerializer):
    class Meta:
        model = FinancialProposal
        fields = ['status']
