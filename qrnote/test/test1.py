import requests

url = 'http://localhost:8000'
r = requests.get(url)

assert r.status_code == 200
