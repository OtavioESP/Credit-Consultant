from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from financial.models import ProposalStatus, ProposalFields, FinancialProposal


class FinancialProposalTests(APITestCase):

    def setUp(self):
        self.proposal_status = ProposalStatus.objects.create(name='Pending')
        self.proposal_fields = ProposalFields.objects.create(
            name='Field 1', enabled=True)
        self.valid_data = {
            'status': self.proposal_status.id,
            'fields': [self.proposal_fields.id],
            'amount': 1000
        }

    def test_create_financial_proposal(self):
        url = reverse('financial-proposal-list')
        response = self.client.post(url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FinancialProposal.objects.count(), 1)

    def test_update_financial_proposal(self):
        financial_proposal = FinancialProposal.objects.create(
            status=self.proposal_status,
        )
        url = reverse('financial-proposal-detail',
                      args=[financial_proposal.id])
        updated_data = {
            'status': self.proposal_status.id,
            'fields': [self.proposal_fields.id],
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_financial_proposals(self):
        FinancialProposal.objects.create(
            status=self.proposal_status,
        )
        url = reverse('financial-proposal-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_financial_proposal(self):
        financial_proposal = FinancialProposal.objects.create(
            status=self.proposal_status,
        )
        url = reverse('financial-proposal-detail',
                      args=[financial_proposal.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProposalStatusViewTests(APITestCase):

    def test_list_proposal_statuses(self):
        url = reverse('proposal-status-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProposalFieldsViewTests(APITestCase):

    def test_list_enabled_proposal_fields(self):
        url = reverse('proposal-fields-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
