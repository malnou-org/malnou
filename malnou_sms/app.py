from flask import json
from flask import jsonify
from flask import request
from flask import Flask
from flask import make_response
from multiprocessing.pool import ThreadPool
import time

from listen import listenNewMessages

app = Flask(__name__)

@app.route('/api/v1.0/listener', methods=['POST'])
def create_listener():
        listenNewMessages()
        return make_response(jsonify(
                {'Status': 'Listener started successfully'}
        ), 200)

@app.route('/api/v1.0/add_new_contacts', methods=['POST'])
def addNewContacts():
        return "TODO"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(debug=True)