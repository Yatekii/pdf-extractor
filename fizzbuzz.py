from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    fizzbuzz = ""
    for x in range(1,100):
        if x % 3 == 0:
            fizzbuzz += "fizz"
        elif x % 5 == 0:
            fizzbuzz += "buzz"
        elif x % 15 ==0:
            fizzbuzz += "fizzbuzz"
        else: 
            fizzbuzz += str(x)
        fizzbuzz += "<br>"
    return fizzbuzz

