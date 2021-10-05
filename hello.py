from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hey guys, this is the top page of this test site</p><br/><a href='/page1'>page1</a><br/><a href='/page2'>page2</a>"

@app.route("/page1")
def page1():
    return "<p>Hi, This is page 1</p><br/><a href='/'>back</a>"

@app.route("/page2")
def page2():
    return "<p>Hi, This is page 13</p><br/><a href='/'>back</a>"

if __name__ == "__main__":
    app.run(host=os.getenv('IP','0.0.0.0'),port=os.getenv('PORT',5000),debug=True)

