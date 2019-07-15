import json
from translate import translate, translator_init
from datetime import datetime

def cleanComplaints(data, keyword):
    # print(data)
    now =  datetime.now()
    message_dict = {}
    for i in data:
        message_date = i["date"]
        message_date = datetime.strptime(message_date, '%Y-%m-%d %H:%M:%S')
        diff = now - message_date
        # print(diff.total_seconds())
        if diff.total_seconds() <= 60 and "COMPLAINT" in i["message"]:
            message = i["message"]
            message = message.replace(keyword, '')
            message = message.replace('COMPLAINT', '')
            translated_message = translate(
                translator_init(),
                message
            )
            message_dict =  {
                    "number": i["number"],
                    "date": i["date"],
                    "complaint": message,
                    "translated": translated_message.text,
                    "class": {
                    }
                }
    return message_dict

