#!/usr/bin/env python3
from flask import Blueprint, send_from_directory,render_template

app = Blueprint('qrcode', __name__,static_folder='static')

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('qrcode.html')

if __name__ == '__main__':
    from flask import Flask
    App = Flask(__name__)
    App.register_blueprint(app,endpoint='qrcode',url_prefix='/qrcode')
    App.run(host='0.0.0.0', port=5000, debug=True)
