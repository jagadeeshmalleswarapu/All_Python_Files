import requests

# BASE_URL = 'http://127.0.0.1:5000/'
BASE_URL = 'http://127.0.0.1:5001/'
name = 'Venkat'
testNum = 200
# response = requests.get(BASE_URL+'helloWorld/'+name+'/'+testNum.__str__())
response = requests.get(BASE_URL+'video/1')

# postt = requests.post(BASE_URL+'helloWorld')

print(response.json())

# print((postt.json()))