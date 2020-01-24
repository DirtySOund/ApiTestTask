from json import JSONDecodeError
import requests


class RequestTypes:
    GET = 'GET'
    POST = 'POST'


def _send_request(request_type, url, request_data=None):
    headers = ''
    assert request_type in RequestTypes.__dict__
    if request_type == RequestTypes.GET:
        response = requests.get(url, json=request_data, headers=headers)
    elif request_type == RequestTypes.POST:
        response = requests.post(url, json=request_data, headers=headers)
    else:
        response = None

    try:
        response_body = response.json()
    except JSONDecodeError:
        response_body = None
    return response.status_code, response_body


class ApiRequests:
    """ Requests """

    def __init__(self, host):
        self.dummy_url = host

    def single_employee_get(self, user_id):
        return _send_request(RequestTypes.GET, url=f'{self.dummy_url}/employee/{user_id}')

    def single_employee_post(self, config):
        return _send_request(RequestTypes.POST, url=f'{self.dummy_url}/create',
                             request_data=config)
