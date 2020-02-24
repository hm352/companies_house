''' connects to streams using python requests
'''
import os

import requests
# from time import sleep


def connect(timepoint):
    '''connects to company house streaming api '''
    params = {'timepoint': timepoint} if timepoint else timepoint
    url = 'https://stream.companieshouse.gov.uk/companies'
    api_key = os.environ.get('API_KEY')
    response = requests.get(
        url,
        auth=(api_key, ''),
        params=params,
        stream=True
    )
    return response


def check_stream():
    ''' checks the connection status code
    and reconnects if not
    '''
    
