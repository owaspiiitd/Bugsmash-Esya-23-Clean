import requests
from bs4 import BeautifulSoup

payload_path = '/test/test_large.png'

response = requests.post('http://127.0.0.1:8000/upload.php', files = {'fileupload' : open(payload_path, 'rb')})
soup = BeautifulSoup(response.content, 'html.parser')
links = [link['href'] for link in soup.find_all('a')]
for link in links:
    assert '.png' not in link
