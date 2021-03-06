# Amanda Chen
# SoftDev1 pd1
# K<n> -- <Title/Topic/Summary>
# <yyyy>-<mm>-<dd>

import os
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

os.path.dirname(__file__)
DIR = os.path.dirname(__file__) or '.'
DIR += '/'

name = "Testing"
roster = "me"

@app.route("/")
def root():
    print(app)
    return render_template('root.html',
                            team = name,
                            rost = roster)

@app.route("/auth")
def authenticate():
    return render_template('out.html',
                            team = name,
                            rost = roster,
                            arg_user = str(request.args["username"]),
                            arg_method = str(request.method))


@app.route("/error")
def err():
    return "blaaa"


if __name__ == "__main__":
    app.debug = True
    app.run()
