from flask import Flask
from markupsafe import escape
import os
import time
from ddtrace import tracer

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hey guys, this is the top page of this test site</p><br/><a href='/page1'>page1</a><br/><a href='/page2'>page2</a>"

@app.route("/page1")
def page1():
    return "<p>Hi, This is page 1</p><br/><a href='/'>back</a>"

@app.route("/<name>")
def routename(name):
    return f"Hello, {escape(name)}!"

@app.route("/methodpage")
def methodpage():
    with tracer.trace("testtrace") as outer_span:
        time.sleep(1)
        with tracer.trace("method1") as span:
            method1()
        time.sleep(1)
        with tracer.trace("method2") as span:
            method2()
    return "<p>Method1 and Method2 run. Please check the console output</p>"


@app.route("/page2")
def page2():
    return "<p>Hi, This is page 16</p><br/><a href='/'>back</a>"

def method1():
    print("Method1 is running....")
    time.sleep(2)
    print("Method1 finished")


def method2():
    print("Method2 is running....")
    time.sleep(3)
    print("Method2 finished")


if __name__ == "__main__":
    app.run(host=os.getenv('IP','0.0.0.0'),port=os.getenv('PORT',5002),debug=True)

