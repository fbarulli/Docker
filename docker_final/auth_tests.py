import os
import requests

api_address = 'api'  # Container name in Docker Compose
api_port = 8000

def run_auth_test(username, password, expected_status):
    r = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params={'username': username, 'password': password}
    )
    status_code = r.status_code
    test_status = 'SUCCESS' if status_code == expected_status else 'FAILURE'
    output = f'''
============================
    Authentication test
============================
request done at "/permissions"
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
    run_auth_test('alice', 'wonderland', 200),
    run_auth_test('bob', 'builder', 200),
    run_auth_test('clementine', 'mandarine', 403)
]

if not all(results):
    exit(1)  # Exit with error if any test fails