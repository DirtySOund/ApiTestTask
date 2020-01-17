import pytest

from libs.api_requests import ApiRequests


@pytest.fixture(scope="session")
def configs():
    api_url = "http://dummy.restapiexample.com/api/v1"
    return api_url


@pytest.fixture(scope='session')
def api_requests(configs):
    return ApiRequests(configs)
