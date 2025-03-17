import os
import requests

api_address = 'api'
api_port = 8000
sentence = 'test sentence'

def run_authz_test(username, password, endpoint, expected_status):
    r = requests.get(
        url=f'http://{api_address}:{api_port}/{endpoint}',
        params={'username': username, 'password': password, 'sentence': sentence}
    )
    status_code = r.status_code
    test_status = 'SUCCESS' if status_code == expected_status else 'FAILURE'
    output = f'''
============================
    Authorization test
============================
request done at "/{endpoint}"
| username="{username}"
| password="{password}"
expected result = {expected_status}
actual result = {status_code}
==> {test_status}
'''
    print(output)
    if os.environ.get('LOG') == '1':
        with open('/app/api_test.log', 'a') as file:
            file.write(output)
    return test_status == 'SUCCESS'

# Run all test cases
results = [
    run_authz_test('bob', 'builder', 'v1/sentiment', 200),
    run_authz_test('bob', 'builder', 'v2/sentiment', 403),
    run_authz_test('alice', 'wonderland', 'v1/sentiment', 200),
    run_authz_test('alice', 'wonderland', 'v2/sentiment', 200)
]

if not all(results):
    exit(1)