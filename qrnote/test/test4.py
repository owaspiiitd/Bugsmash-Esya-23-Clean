import requests
import os
from bs4 import BeautifulSoup
from pyzbar import pyzbar
from PIL import Image

url = 'http://localhost:8000'

def make_post():
    res = requests.post(url, data={'content': 's3cr3t_c0nt3nt'})
    soup = BeautifulSoup(res.content, 'html.parser')
    qrcode_url = soup.find_all('img')[1]['src']
    codes = pyzbar.decode(Image.open('/app' + qrcode_url))
    if codes[0].type == 'QRCODE':
        payload = codes[0].data.decode()
        return payload
    return ''

payloads = list()
while len(payloads) != 5:
    payloads.append(make_post())
id_order = payloads
id_order.sort()
for i in range(5):
    assert payloads[i] != id_order[i]
