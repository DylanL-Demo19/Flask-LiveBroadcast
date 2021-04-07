from flask import Flask, render_template
from flask_sockets import Sockets

app = Flask(__name__)
app.debug = True
sockets = Sockets(app)


@sockets.route('/echo')
def echo_scoket(ws):
    while True:
        message = ws.receive()
        if message == "socket open!":
            ws.send("Start to use Chatbot.")
        else:
            ws.send(message)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/echo_test', methods=['GET'])
def echo_test():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8000
    )
