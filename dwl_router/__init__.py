import os
import logging
from flask import Flask, request

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        MODE=os.getenv('FLASK_ENV'),
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'


    @app.route('/rgleads', methods=['GET', 'POST'])
    def log_leadrouter_lead():
        '''log information from lead router'''
        if request.method == 'POST':
            app.logger.info(request.get_json())
            return 'Lead Received'
        else:
            return 'This route accepts POST requests from the lead router.'


    return app
