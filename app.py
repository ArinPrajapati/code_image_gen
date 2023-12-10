# app.py

from flask import Flask, render_template

app = Flask(__name__)
PLACEHOLDER_CODE = "print('Hello, World!')"


@app.route("/", methods=["GET"])
def code():
    context = {
        "message": "Paste your python code 🐍"
       , "code": PLACEHOLDER_CODE
    ,}
    return render_template("code_input.html", **context)
