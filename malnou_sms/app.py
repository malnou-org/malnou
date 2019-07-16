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
from TextLocal.sendMessage import sendSMS
from configparser import ConfigParser

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

@app.route('/api/v1.0/sendMessages', methods=['POST'])
def sndMssg():
        if not request.json:
                abort(400)
        cfg = ConfigParser()
        cfg.read('config.ini')
        return sendSMS(cfg.get('TextLocalKeys', 'TextLocal_api_key'), request.json["numbers"], request.json["message"])

@app.route('/api/v1.0/sendDefaultMessages', methods=['POST'])
def sndDefaultMssg():
        if not request.json:
                abort(400)
        if request.json["message_type"] == "GreetingMessage":
                req_list_id = 0
        elif request.json["message_type"] == "FoodPlan":
                req_list_id = 1
        elif request.json["message_type"] == "Assurance":
                req_list_id = 2
        elif request.json["message_type"] == "Reply":
                req_list_id = 3
        else:
                abort(400)
        message = getDefaultMessages()["messages"][req_list_id]["message"]
        cfg = ConfigParser()
        cfg.read('config.ini')
        return sendSMS(cfg.get('TextLocalKeys', 'TextLocal_api_key'), request.json["numbers"], message)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
        p = Process(target=listenNewMessages)
        p.start()  
        app.run(debug=True, use_reloader=False)
        p.join()
