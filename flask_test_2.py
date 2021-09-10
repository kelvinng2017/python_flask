from flask import Flask

app = Flask(__name__)

@app.route("/<name>")
def flask(name):
	return "Hello "+name+"!"

@app.route("/")
def test():
	return "Hello World!"

if __name__ == "__main__":
    app.run(host="192.168.0.85", port=8888, debug=True)
