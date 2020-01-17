import logging
from json import JSONDecodeError

import allure
import requests

logger = logging.getLogger(__name__)


class RequestTypes:
    GET = 'GET'
    POST = 'POST'
    DELETE = 'DELETE'


def _send_request(request_type, url, request_data=None, custom_header=None, auth=False, auth_user=None):
    _log_request(request_type, url, request_data)
    headers = ''
    if custom_header:
        headers = custom_header
    elif auth and not custom_header:
        if auth_user is not None:
            headers = {'Authorization': ''}
    assert request_type in RequestTypes.__dict__

    if request_type == RequestTypes.GET:
        response = requests.get(url, json=request_data, headers=headers)
    elif request_type == RequestTypes.POST:
        response = requests.post(url, json=request_data, headers=headers)
    else:
        response = requests.delete(url, json=request_data, headers=headers)

    try:
        response_body = response.json()
    except JSONDecodeError:
        response_body = None

    _log_response(response.status_code, response_body)
    return response.status_code, response_body


@allure.step(title="request")
def _log_request(request_type, url, request_data):
    logger.info(f'Request: {request_type} {url} Body: {request_data}')


@allure.step(title="response")
def _log_response(response_code, response_data):
    logger.info(f'Response: {response_code} {response_data}')


class ApiRequests:
    """ Api requests """

    def __init__(self, host):
        self.dummy_url = host

    """ MVP requests """

    def single_employee_try_get(self, user_id, custom_cache=None):
        return _send_request(RequestTypes.GET, url=f'{self.dummy_url}/employee/{user_id}', custom_header=custom_cache)

    def single_employee_get(self, user_id):
        status_code, response_data = self.single_employee_try_get(user_id)
        assert status_code == 200, f'Wrong response status code: {status_code}'
        return response_data

    def single_employee_try_post(self, config, custom_cache=None):
        return _send_request(RequestTypes.POST, url=f'{self.dummy_url}/create',
                             request_data=config, custom_header=custom_cache)

    def single_employee_post(self, config):
        status_code, response_data = self.single_employee_try_post(config)
        assert status_code == 200, f'Wrong response status code: {status_code}'
        return response_data
