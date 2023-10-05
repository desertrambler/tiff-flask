from flask import Flask, render_template, url_for, request, abort, jsonify

app = Flask(__name__)

@app.route("/")
def render_index():
    return render_template("index.html")


with app.test_request_context():
    url_for('static', filename='styles.css')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) # make sure port is > 5000

