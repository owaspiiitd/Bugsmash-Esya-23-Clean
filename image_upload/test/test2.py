import requests
from bs4 import BeautifulSoup

payload_path = '/test/test_small.png'

response = requests.post('http://127.0.0.1:8000/upload.php', files = {'fileupload' : open(payload_path, 'rb')})
soup = BeautifulSoup(response.content, 'html.parser')
links = [link['href'] for link in soup.find_all('a')]
assert len(links) != 0
payload_link = links[0]
response = requests.get('http://127.0.0.1:8000/' + payload_link)
assert response.status_code == 200
with open(payload_path, 'rb') as f:
    assert f.read() == response.content
