from flask import json
from flask import jsonify
from flask import request
from flask import Flask
from flask import abort
from flask import make_response
from multiprocessing import Process, Value
import time

from listen import listenNewMessages
from setDefaultMessages import setDefaultMessages
from getDefaultMessages import getDefaultMessages

app = Flask(__name__)

@app.route('/api/v1.0/set_messages', methods=['POST'])
def setMessages():
        if not request.json or not 'messages' in request.json:
                abort(400)
        for reqs in request.json["messages"]:
                if reqs["name"] == "GreetingMessage":
                        req_list_id = 0
                elif reqs["name"] == "FoodPlan":
                        req_list_id = 1
                elif reqs["name"] == "Assurance":
                        req_list_id = 2
                elif reqs["name"] == "Reply":
                        req_list_id = 3
                else:
                        abort(400)
                setDefaultMessages(reqs["message"], req_list_id)
        return jsonify(getDefaultMessages()), 201

@app.route('/api/v1.0/get_messages', methods=['GET'])
def getMessages():
        return jsonify(getDefaultMessages())


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
        p = Process(target=listenNewMessages)
        p.start()  
        app.run(debug=True, use_reloader=False)
        p.join()
