from flask import Flask
import socket
app = Flask(__name__)


@app.route("/")
def test():
    return "<h1>Hello World!</h1>"


if __name__ == "__main__":
    # can change to app.run(host=ip you need ,port="port youneed",debug=True)
    # get computer name
    # use computer name get ip
    app.run(host="192.168.0.85", port=8888, debug=True)
