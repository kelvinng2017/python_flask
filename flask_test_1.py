from flask import Flask

app = Flask(__name__)

@app.route("/Flask")
def flask():
    return "Hello Flask!"

@app.route("/")    
def test():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="192.168.0.85", port=8888, debug=True)
