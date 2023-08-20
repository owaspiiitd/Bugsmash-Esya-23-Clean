import requests
import os,sys

r = requests.get("http://127.0.0.1:5000/test/SuperSecurePass@123")
if (r.text == "SuperSecurePass@123-PASS{SuperSecurePass@123}"):
    if(os.path.exists("/home/password.txt")):
        print("Fail")
    else:
        sys.exit(0)
else:
    print("Fail")
