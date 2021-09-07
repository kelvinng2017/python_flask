from flask import Flask
import socket
app = Flask(__name__)


@app.route("/")
def test():
    return "Hello World!"


if __name__ == "__main__":
    # can change to app.run(host=ip you need ,port="port youneed",debug=True)
    # get computer name
    # use computer name get ip
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    app.run(host="192.168.1.105", port=8787, debug=True)
