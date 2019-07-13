import json


def cleanComplaints(data):
    message_dict = {}
    for i in data:
        if i["isNew"] == True and "COMPLAINT" in i["message"]:
            message = i["message"]
            message = message.replace('AHW4L', '')
            # print(message)
            message_dict =  {
                    "number": i["number"],
                    "date": i["date"],
                    "complaint": message,
                    "class": {
                    }
                }
    return message_dict

