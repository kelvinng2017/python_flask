from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/<name>")
def test(name=None):
	if name==None:
		return "Hello World!"
	return "Hellow "+name+"!"
if __name__ == "__main__":
    app.run(host="192.168.0.85", port=8888, debug=True)
