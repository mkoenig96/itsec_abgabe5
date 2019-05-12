import requests
r = requests.get('http://localhost:9090/')
print(r.text)
