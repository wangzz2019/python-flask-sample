from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/page1")
def page1():
    return "<p>Hi, This is page 1</p>"

@app.route("/page2")
def page2():
    return "<p>Hi, This is page 12</p>"

if __name__ == "__main__":
    app.run(host=os.getenv('IP','127.0.0.1'),port=int(os.getenv('PORT',5000)),debug=True)

