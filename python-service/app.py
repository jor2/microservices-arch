from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify
from utils import invoke_service


app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route("/")
def index():
    return jsonify("Hello Wold!")


@app.route("/javascript")
def javascript_response():
    return jsonify(invoke_service(service="javascript-service").content.decode())


@app.route("/go")
def go_response():
    return jsonify(invoke_service(service="go-service").content.decode())


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True, host='0.0.0.0')
