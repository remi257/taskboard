import requests

url = 'http://localhost:8081/tasks/complete/R3EZ'

x = requests.post(url)

print(x.text)