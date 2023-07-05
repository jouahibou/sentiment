import os 
import requests

api_address = '127.0.0.1'
api_port = 8000

users = [
        {'username':'alice','password':'wonderland'},
        {'username':'bob','password':'builder'},
        {'username':'clementine','password':'mandarine'}
         ]
for user in users:
    r= requests.get(
    url = 'http://{address}:{port}/permissions'.format(address=api_address,port=api_port),
    params = user
)
    output = '''
    ============================
        Authentication test
    ============================

    request done at "/permissions"
    | username="{username}"
    | password="{password}"

    expected result = 200
    actual restult = {status_code}

    ==>  {test_status}

    '''
    status_code = r.status_code

    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(username =user['username'] ,password = user['password'],status_code=status_code,test_status=test_status))

    if os.environ.get('LOG') == 1 : 
        with open('api_test.log','a') as file:
            file.write(output.format(username=user['username'],password=user['password'], status_code=status_code,test_status=test_status))        