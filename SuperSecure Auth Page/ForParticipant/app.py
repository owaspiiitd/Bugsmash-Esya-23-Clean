from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Admin Page")

@app.route("/greet/<name>")
def hello_world_greet(name):
    return f"Hello, {name}!, Welcome to the SuperSecure Portal "+ "You are free to submit the code now."

@app.route("/calc/", methods=['GET', 'POST'])
def hello_world_calc():
    password = request.form.get('password')
    print(":"+password+":")
    filePass=""
    try:
        fo = open("password.txt", "r")
        filePass = fo.read()
        print(filePass)
    except:
        print("File io error")  

    if(filePass==password):
        return hello_world_greet("admin")
    else:
        return "Strings did not match -- Try Again"
    

# DO NOT change the below functions     
@app.route("/test/<password>")
def test(password):
    filePass=""
    try:
        fo = open("password.txt", "r")
        filePass = fo.read()
    except:
        print("File io error")  

    if(filePass==password):
        return "SuperSecurePass@123-PASS{"+filePass+"}"
    else:
        return "Strings did not match -- Try Again"

@app.route("/test/")
def test_blank():
    filePass=""
    try:
        fo = open("password.txt", "r")
        filePass = fo.read()
    except:
        print("File io error")  

    if(filePass==""):
        return "SuperSecurePass@123-PASS{"+filePass+"}"
    else:
        return "Strings did not match -- Try Again"
