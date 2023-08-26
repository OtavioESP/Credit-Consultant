import requests


class ProposalValuation:

    def __init__(self):
        self._API_URL = 'https://loan-processor.digitalsys.com.br'

    def check_proposal(self, data) -> bool:
        '''
            endpoint returns {"approved": bool}
            So based on the bool it return to the view
            If the request wasnt sucessful it can presume any kind of return
        '''
        response = requests.post(f'{self._API_URL}/api/v1/loan', data=data)

        if response.status_code == 200:
            return response.json().get('approved')

        return False
