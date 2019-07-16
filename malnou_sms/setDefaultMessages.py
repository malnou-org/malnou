import json

def setDefaultMessages(req_message, req_msg_id):
    with open('messages.json', 'r') as json_file:  
        data = json.load(json_file)
        data["messages"][req_msg_id]["message"] = req_message
        json_file.close()
    with open('messages.json', 'w') as json_file:
        json.dump(data, json_file)

