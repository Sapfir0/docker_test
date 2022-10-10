from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    with open('counter.txt', 'r') as f:
        counter = int(f.readline())
        return str(counter)
    

@app.route("/stat")
def stat():
    line = 0

    with open('counter.txt', 'r+') as f:
        line = f.readline()
        f.seek(0)
        counter = int(line)
        stringCounter = str(counter + 1)
        f.write(stringCounter)
        return stringCounter

@app.route("/about")
def about():
    return "<h3> Hello, Alexander Yurev </h3>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)