from flask import Flask

app = Flask(__name__)
@app.route("/index1 ")
def home():
    return "Hi there"
app.run()