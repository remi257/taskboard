import requests

url = 'http://localhost:8081/tasks/get'

x = requests.get(url)

print(x.text)