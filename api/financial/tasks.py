import requests
import json

from celery import shared_task

from person.models import Person

from financial.enums import ProposalStatusEnum
from financial.models import FinancialProposal

API_URL = 'https://loan-processor.digitalsys.com.br'


@shared_task()
def check_proposal_availability(data: dict) -> bool:
    '''
        Fetch the data, and concatenate request response into the data
    '''
    response = requests.post(f'{API_URL}/api/v1/loan', data=data)

    if response.status_code == 200:

        data['approved'] = response.json().get('approved', '')
        string_data = json.dumps(data)

        financial_proposal = FinancialProposal.objects.create(
            proposal_data=string_data
        )

        if response.json().get('approved'):
            financial_proposal.status_id = ProposalStatusEnum.HUMAM_APPROVAL
        else:
            financial_proposal.status_id = ProposalStatusEnum.DENIED

        if data.get('person', None):
            financial_proposal.person = Person.objects.get(id=data['person'])

        financial_proposal.save()

        return response.json().get('approved')

    return False
