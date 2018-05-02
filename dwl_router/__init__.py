import logging
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/rgleads', methods=['GET', 'POST'])
def log_leadrouter_lead():
    '''log information from lead router'''
    app.logger.info(request.get_json())
    return 'Lead Received'
