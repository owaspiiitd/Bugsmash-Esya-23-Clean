import requests

r = requests.get("http://127.0.0.1:5000/test/SuperSecurePass@123")
if (r.text == "SuperSecurePass@123-d4rkc0de-PASS{SuperSecurePass@123}"):
    print("Pass")
else:
    print("Fail")
