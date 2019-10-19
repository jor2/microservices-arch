from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route("/")
def index():
    return jsonify("Hello Wold!")


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True, host='0.0.0.0')
