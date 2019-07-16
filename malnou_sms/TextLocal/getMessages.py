#!/usr/bin/env python
 
import urllib.request
import urllib.parse
import json
 
def getMessages(apikey, inboxID):
    data =  urllib.parse.urlencode({'apikey': apikey, 'inbox_id' : inboxID})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/get_messages/?")
    f = urllib.request.urlopen(request, data)
    respData = json.loads(f.read())
    return(respData)
 