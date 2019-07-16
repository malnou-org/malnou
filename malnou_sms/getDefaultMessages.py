import json

def getDefaultMessages():
    with open('messages.json') as json_file:  
        data = json.load(json_file)
    return data
    