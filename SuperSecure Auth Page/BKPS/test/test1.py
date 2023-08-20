import requests

r = requests.get("http://127.0.0.1:5000/calc/3 + 4")
if (r.text == "7"):
    print("pass")
else:
    print("fail")
