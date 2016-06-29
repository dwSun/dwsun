#!/usr/bin/env python3
from flask import Flask, send_from_directory,render_template
from flask_debugtoolbar import DebugToolbarExtension

from qrcode import app as qr

app = Flask(__name__)
app.config["SECRET_KEY"] = "6169d7cc-3e0b-11e6-b736-90004ed04be2"

dtoolb = DebugToolbarExtension(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

#app.register_blueprint(uploads,endpoint='uploads',url_prefix='/cmdsaver')
app.register_blueprint(qr,endpoint='qrcode',url_prefix='/qrcode')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
