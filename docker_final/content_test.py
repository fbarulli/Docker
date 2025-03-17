import os
import requests

api_address = 'api'
api_port = 8000
username = 'alice'
password = 'wonderland'

def run_content_test(endpoint, sentence, expected_sign):
    r = requests.get(
        url=f'http://{api_address}:{api_port}/{endpoint}',
        params={'username': username, 'password': password, 'sentence': sentence}
    )
    status_code = r.status_code
    if status_code != 200:
        score = None
        test_status = 'FAILURE'
    else:
        score = r.json().get('score', 0)
        test_status = 'SUCCESS' if (score * expected_sign > 0) else 'FAILURE'
    output = f'''
============================
    Content test
============================
request done at "/{endpoint}"
| sentence="{sentence}"
expected sentiment = {'positive' if expected_sign > 0 else 'negative'}
actual score = {score}
==> {test_status}
'''
    print(output)
    if os.environ.get('LOG') == '1':
        with open('/app/logs/api_test.log', 'a') as file:
            file.write(output)
    return test_status == 'SUCCESS'

# Run all test cases
results = [
    run_content_test('v1/sentiment', 'life is beautiful', 1),
    run_content_test('v1/sentiment', 'that sucks', -1),
    run_content_test('v2/sentiment', 'life is beautiful', 1),
    run_content_test('v2/sentiment', 'that sucks', -1)
]

if not all(results):
    exit(1)