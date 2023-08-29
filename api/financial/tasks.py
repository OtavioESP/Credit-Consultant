import requests

from celery import shared_task

from person.models import Person

from financial.enums import ProposalStatusEnum
from financial.models import FinancialProposal

API_URL = 'https://loan-processor.digitalsys.com.br'


@shared_task()
def check_proposal_availability(data: dict) -> bool:
    '''
        endpoint returns {"approved": bool}
        So based on the bool it return to the view
        If the request wasnt sucessful it can presume any kind of return
    '''
    response = requests.post(f'{API_URL}/api/v1/loan', data=data)

    financial_proposal = FinancialProposal.objects.create(
        proposal_data=response.json()
    )
    print('\n\n\n\n\n\n\n')
    print(data)
    print('\n\n\n\n\n\n\n')
    if data.get('person', None):
        financial_proposal.person = Person.objects.get(id=data['person'])
    financial_proposal.save()

    if response.status_code == 200:

        if response.json().get('approved'):
            financial_proposal.status_id = ProposalStatusEnum.HUMAM_APPROVAL
            financial_proposal.save()
        else:
            financial_proposal.status_id = ProposalStatusEnum.DENIED
            financial_proposal.save()
        return response.json().get('approved')
    return False
