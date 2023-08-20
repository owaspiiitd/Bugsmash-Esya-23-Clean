import requests

r = requests.get("http://127.0.0.1:5000/test/")
if (r.text == "Strings did not match -- Try Again"):
    print("Pass")
else:
    print("Fail")
