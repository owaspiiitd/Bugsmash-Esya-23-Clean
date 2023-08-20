from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Admin Page")

@app.route("/greet/<name>")
def hello_world_greet(name):
    return f"Hello, {name}!, Welcome to the SuperSecure Login Page"

@app.route("/calc/", methods=['GET', 'POST'])
def hello_world_calc():
    password = request.form.get('password')
    filePass=""
    try:
        fo = open("password.txt", "r")
        filePass = fo.read()
        print(filePass)
    except:
        print("File io error")  

    if(filePass==password):
        return f"Hello, admin!, Welcome to the SuperSecure Portal"
    else:
        return "Strings did not match -- Try Again"

    # print(password)
    
    
