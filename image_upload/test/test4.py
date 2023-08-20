import requests
from bs4 import BeautifulSoup

payload = '<?php echo exec("echo s3cr3t"); ?>'
payload_path = '/tmp/cmd.php'
with open(payload_path, 'w') as f:
    f.write(payload)

response = requests.post('http://127.0.0.1:8000/upload.php', files = {'fileupload' : open(payload_path, 'rb')})
soup = BeautifulSoup(response.content, 'html.parser')
links = [link['href'] for link in soup.find_all('a')]
for link in links:
    assert '.php' not in link
