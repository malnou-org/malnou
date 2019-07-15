import os
import json
import time

from TextLocal.getMessages import getMessages
from TextLocal.getInbox import getInboxes
from Firebase.firebaseInit import firebaseInit
from Firebase.firebasePush import firebasePush
from cleanComplaints import cleanComplaints


TextLocal_api_key = '****'
TextLocal_keyWord = '****'

def listenNewMessages():
    dbRef = firebaseInit()

    inboxID = getInboxes(TextLocal_api_key)

    while True:
        # print("New Loop")
        messages = getMessages(TextLocal_api_key, inboxID)
        messages = messages['messages']
        # print(messages)
        messages = cleanComplaints(messages, TextLocal_api_key)
        # print(messages)
        firebasePush(messages, dbRef)
        time.sleep(10)