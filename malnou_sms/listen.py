import os
import json
import time

from TextLocal.getMessages import getMessages
from TextLocal.getInbox import getInboxes
from Firebase.firebaseInit import firebaseInit
from Firebase.firebasePush import firebasePush
from cleanComplaints import cleanComplaints
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini')

TextLocal_api_key = cfg.get('TextLocalKeys', 'TextLocal_api_key')
TextLocal_keyWord = cfg.get('TextLocalKeys', 'TextLocal_keyWord')
FirebaseUrl = cfg.get('Firebase', 'FirebaseUrl')
FirebaseJson = cfg.get('Firebase', 'JsonFilePath')

def listenNewMessages():
    dbRef = firebaseInit(FirebaseUrl, FirebaseJson)

    inboxID = getInboxes(TextLocal_api_key)

    while True:
        print("1 loop")
        messages = getMessages(TextLocal_api_key, inboxID)
        messages = messages['messages']
        # print(messages)
        messages = cleanComplaints(messages, TextLocal_keyWord)
        # print(messages)
        firebasePush(messages, dbRef)
        time.sleep(60)