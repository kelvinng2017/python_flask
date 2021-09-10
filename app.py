from flask import Flask,render_template
from flask.helpers import url_for
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

"""
@app.route('/second')
def test():
    return render_template('stkmove.html')
"""
"""
@app.route('/second')
def test():
    return url_for('index')
"""
@app.route('/second')
def test():
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(host="192.168.0.85", port=8888, debug=True)

