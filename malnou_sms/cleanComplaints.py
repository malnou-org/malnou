import json
from translate import translate, translator_init
from datetime import datetime

from Watson.watsonNLU import watsonNLU
from configparser import ConfigParser

def cleanComplaints(data, keyword):
    cfg = ConfigParser()
    cfg.read('config.ini')
    # print(data)
    now =  datetime.now()
    message_dict = {}
    for i in data:
        message_date = i["date"]
        message_date = datetime.strptime(message_date, '%Y-%m-%d %H:%M:%S')
        diff = now - message_date
        # print(diff.total_seconds())
        if (diff.total_seconds() <= 60 or i["isNew"] == True) and "COMPLAINT" in i["message"]:
            message = i["message"]
            message = message.replace(keyword, '')
            message = message.replace('COMPLAINT', '')
            translated_message = translate(
                translator_init(),
                message
            )
            insights = watsonNLU(
                cfg.get('WatsonNLU', 'version'),
                cfg.get('WatsonNLU', 'apikey'),
                cfg.get('WatsonNLU', 'url'),
                cfg.get('WatsonNLU', 'modelID'),
                translated_message.text
            )
            message_dict =  {
                    "number": i["number"],
                    "date": i["date"],
                    "complaint": message,
                    "translated": translated_message.text,
                    "keywords": insights['keywords'],
                    "entities": insights['entities']
                }
    return message_dict

