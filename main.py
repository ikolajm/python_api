import requests

url = 'http://randomfox.ca/floof'

response = requests.get(url)
print(response.status_code)
print(response.json())

fox = response.json()
print(fox['image'])