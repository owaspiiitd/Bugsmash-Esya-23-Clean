import requests
import os
from bs4 import BeautifulSoup
from pyzbar import pyzbar
from PIL import Image

url = 'http://localhost:8000'

res = requests.post(url, data={'content': 's3cr3t_c0nt3nt'})
assert res.status_code == 200
soup = BeautifulSoup(res.content, 'html.parser')
qrcode_url = soup.find_all('img')[1]['src']
codes = pyzbar.decode(Image.open('/app' + qrcode_url))
assert codes[0].type == 'QRCODE'
res = requests.post(url, files={'ticket': ('qr.png', open('/app'+qrcode_url, 'rb'), 'image/png')})
assert 's3cr3t_c0nt3nt' not in res.text
