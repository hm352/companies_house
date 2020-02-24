''' connects to streams using python requests
'''
import os

import requests
from time import sleep

from timepoint import get_timepoint


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


def check_stream(stream):
    ''' checks the connection status code
    and reconnects if not
    '''
    status = stream.status_code
    timepoint = get_timepoint()

    if status == 401:
        print('unathroised, check api key')

    if status == 429:
        sleep(60)
        print('waited')
        return connect(timepoint)

    if status == 416:
        print('timepoint invalid')
        return connect(None)

    return stream