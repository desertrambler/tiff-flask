from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

with app.test_request_context():
    url_for('static', filename='styles.css')


