import time
import sys
import uuid
import argparse
import ibmiotf.device
import wiotp.sdk.device
from configparser import ConfigParser



def commandProcessor(cmd):
    print("Command received: %s" % cmd.data)

def myOnPublishCallback():
    print("Confirmed event received by IoTF\n")

def sendToCloud(data):
    authMethod = None

    cfg = ConfigParser()
    cfg.read('device.cfg')

    deviceOptions = {
        "identity": {"orgId": cfg.get('device', 'org'), 
                    "typeId": cfg.get('device', 'type'), 
                    "deviceId": cfg.get('device', 'id')},
        "auth": {"token": cfg.get('device', 'auth-token')},
    }
    deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
    deviceCli.commandCallback = commandProcessor

    # Connect and send datapoint(s) into the cloud
    deviceCli.connect()


    success = deviceCli.publishEvent("Child_screening", "json", data, qos=0, onPublish=myOnPublishCallback)
    if not success:
        print("Not connected to IoTF")

    # Disconnect the device and application from the cloud
    deviceCli.disconnect()
