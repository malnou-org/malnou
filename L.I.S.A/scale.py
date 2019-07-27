from __future__ import print_function
import argparse
import binascii
import time
import os
import sys
import json


from bluepy import btle
from datetime import datetime
from Distance import getMeanHeight

import Body_Metrics

text_file = open("config.txt", "r")
MISCALE_MAC = text_file.readlines()[0]


class ScanProcessor():
    def __init__(self,variable1,variable2):
        self.dob=variable1
        self.sex=variable2
    def GetAge(self, d1):
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(datetime.today().strftime('%Y-%m-%d'),'%Y-%m-%d')
        return abs((d2 - d1).days)/365

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if dev.addr == MISCALE_MAC.lower() and isNewDev:
            # print ('  Device: %s (%s), %d dBm %s. ' %
                   # (
                       # ANSI_WHITE + dev.addr + ANSI_OFF,
                       # dev.addrType,
                       # dev.rssi,
                       # ('' if dev.connectable else '(not connectable)'))
                   # , end='')
            for (sdid, desc, data) in dev.getScanData():
                ### Xiaomi V1 Scale ###
#                if data.startswith('1d18') and sdid == 22:
#                    measunit = data[4:6]
#                    measured = int((data[8:10] + data[6:8]), 16) * 0.01
#                    unit = ''
#
#                    if measunit.startswith(('03', 'b3')): unit = 'lbs'
#                    if measunit.startswith(('12', 'b2')): unit = 'jin'
#                    if measunit.startswith(('22', 'a2')): unit = 'kg' ; measured = measured / 2
#
#                    if unit:
#                        print(measured, unit)
#                    else:
#                        print("Scale is sleeping.")

                ### Xiaomi V2 Scale ###
                if data.startswith('1b18') and sdid == 22:
                    measunit = data[4:6]
                    measured = int((data[28:30] + data[26:28]), 16) * 0.01
                    unit = ''

                    if measunit == "03": unit = 'lbs'
                    if measunit == "02": unit = 'kg' ; measured = measured / 2
                    mitdatetime = datetime.strptime(str(int((data[10:12] + data[8:10]), 16)) + " " + str(int((data[12:14]), 16)) +" "+ str(int((data[14:16]), 16)) +" "+ str(int((data[16:18]), 16)) +" "+ str(int((data[18:20]), 16)) +" "+ str(int((data[20:22]), 16)), "%Y %m %d %H %M %S")
                    miimpedance = str(int((data[24:26] + data[22:24]), 16))



                    if unit:
                        height = getMeanHeight()
                        age = self.GetAge(self.dob)

                        lib = Body_Metrics.bodyMetrics(measured, float(height), int(age), self.sex, int(miimpedance))
                        data = {
                            "Weight": measured,
                            "Height": height,
                            "Impedence": miimpedance,
                            "LBM" : lib.getLBMCoefficient(),
                            "Body_fat_percentage" : lib.getFatPercentage(),
                            "Water_percentage" : lib.getWaterPercentage(),
                            "Protein_percentage" : lib.getProteinPercentage(),
                            "Bone_mass" : lib.getBoneMass(),
                            "Muscle_mass" : lib.getMuscleMass(),
                            "Visceral_mass" : lib.getVisceralFat(),
                            "BMI" : lib.getBMI(),
                            "BMR" : lib.getBMR(),
                            "Body_type" : lib.getBodyTypeScale()[int(lib.getBodyType())]
                        }
                        with open('scaleData.json', 'w') as outfile:
                            json.dump(data, outfile)
                    else:
                        print("Scale is sleeping.")


            if not dev.scanData:
                print ('\t(no data)')
            
def save_json(dob,sex):
    scanner = btle.Scanner().withDelegate(ScanProcessor(dob,sex))

    devices = scanner.scan(5)
    
    