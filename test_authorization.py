import os 
import requests

api_address = '127.0.0.1'
api_port = 8000

users = [
        {'username':'alice','password':'wonderland'},
        {'username':'bob','password':'builder'}
         ]

urls = [
    "http://{address}:{port}/v1/sentiment",
    "http://{address}:{port}/v2/sentiment"
]
for user in users:
    print("Testing user :",user['username'])
    for url in urls:
        full_url = url.format(address=api_address,port= api_port)
        r= requests.get(full_url,params=user,auth=(user['username'],user['password'])
        
    )
        output = '''
        ============================
            Authorization test
        ============================

        request done at {url}
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