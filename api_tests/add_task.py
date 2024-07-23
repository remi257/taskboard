import requests

url = 'http://localhost:8081/tasks/add'

x = requests.post(url, json = {'name': 'test task X'})

print(x.text)