import requests
import os,sys

r = requests.get("http://127.0.0.1:5000/test/")
if (r.text == "Strings did not match -- Try Again"):
    if(os.path.exists("/home/password.txt")):
        print("Fail")
    else:
        sys.exit(0)
else:
    print("Fail")
