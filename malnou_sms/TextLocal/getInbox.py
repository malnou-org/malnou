#!/usr/bin/env python
 
import urllib.request
import urllib.parse
import json
 
def getInboxes(apikey):
    data =  urllib.parse.urlencode({'apikey': apikey})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/get_inboxes/?")
    f = urllib.request.urlopen(request, data)
    respData = json.loads(f.read())
    return(respData['inboxes'][0]['id'])
 
# resp =  getInboxes('IaDAaeP28tI-I2ZXRXruU4OU9A9LcVQApEVBiAIXFL')

# print (resp['inboxes'][0]['id'])