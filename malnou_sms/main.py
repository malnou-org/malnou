import os
import json
import time
from iteration_utilities import unique_everseen

from TextLocal.getMessages import getMessages
from TextLocal.getInbox import getInboxes
from Firebase.firebaseInit import firebaseInit
from Firebase.firebasePush import firebasePush
from cleanComplaints import cleanComplaints

TextLocal_api_key = '****'
TextLocal_keyWord = '***'

# newuser = False
dbRef = firebaseInit()

inboxID = getInboxes(TextLocal_api_key)

while True:
    print("New Loop")
    messages = getMessages(TextLocal_api_key, inboxID)
    messages = messages['messages']
    print(messages)
    messages = cleanComplaints(messages)
    print(messages)
    firebasePush(messages, dbRef)
    time.sleep(10) 