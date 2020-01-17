from libs import random
from libs.utils import Step


def test_api_simple_requests(api_requests):
    with Step('1. Create new user'):
        config = random.random_user()
        response_data= api_requests.single_employee_post(config)
        user_id = response_data['data']['id']
        api_requests.single_employee_get(user_id)


def test_api_mvp(api_requests):
    with Step('1. Create new user'):
        config = random.random_user()
        user_name, user_salary, user_age = config['name'], config['salary'], config['age']
        status_code, response_data = api_requests.single_employee_try_post(config)
        assert response_data['status'] == "success"
        assert status_code == 200
        user_id = response_data['data']['id']

    with Step('2. Get created user'):
        status_code = api_requests.single_employee_try_get(user_id)
        assert response_data['status'] == "success"
        assert len(response_data['data']) == 4
        assert response_data['data']['name'] == user_name
        assert response_data['data']['salary'] == user_salary
        assert response_data['data']['age'] == user_age
        assert response_data['data']['id'] == user_id
        assert status_code[0] == 200


def test_api_error_handling(api_requests):
    with Step('1. Try post new user with empty body'):
        config = ''
        status_code = api_requests.single_employee_try_post(config)
        assert status_code[0] == 520

    with Step('2. Try post new user with not full body'):
        config = {"salary": "123", "age": "23"}
        status_code = api_requests.single_employee_try_post(config)
        assert status_code[0] == 200

    with Step('3. Try get user with incorrect user_id'):
        user_id = '/'
        status_code = api_requests.single_employee_try_get(user_id)
        assert status_code[0] == 404

    with Step('4. Try get user with un-existing user_id'):
        user_id = '1111111111'
        status_code = api_requests.single_employee_try_get(user_id)
        assert status_code[0] == 200
