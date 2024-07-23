import requests

url = 'http://localhost:8081/tasks/reset/all'

x = requests.post(url)

print(x.text)