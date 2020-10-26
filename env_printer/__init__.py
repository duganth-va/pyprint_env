from flask import jsonify
from flask import Flask
import os
import json

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    
    @app.route('/')
    def index():
        b = {}
        f = open("/tmp/test", 'r')
        b["FILE_CONTENTS"] = f.read()
        for k, v in os.environ.items():
            b[k] = v
        return jsonify(b)
    return app
