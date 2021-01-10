import time
import os

from flask import Flask, render_template

from socket import socket, AF_INET, SOCK_STREAM, MSG_WAITALL

PORT=1309

def run():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("", PORT))
    s.listen()
    print("Waiting for accept..")
    rs, rs_info = s.accept()
    while True:
        print("Waiting for message..")
        data = rs.recv(1024)
        if not data:
            break
        print(f"Got message: {data}")
        breakpoint()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def ping():

    os.environ['FLASK_ENV'] = "development"
    app.run("0.0.0.0", debug=True)
    #s = socket(AF_INET, SOCK_STREAM)
    #s.connect(("", PORT))
    #s.send(("HELLO"*1024*2).encode('utf-8'))
    #breakpoint()



