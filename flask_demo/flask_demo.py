from flask import Flask
from flask import Flask, render_template
 

app = Flask(__name__)
@app.route("/index1")
def home():
    return render_template("index1.html")
@app.route("/SayHello/<kasem>")
def say_hello(name):
    return f(" Hello {name} ")
app.run()