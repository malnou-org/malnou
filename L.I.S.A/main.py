import os
import subprocess
import json
import time
from pathlib import Path
import csv

from client import sendToCloud
from scale import save_json
from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *

pn532 = Pn532_i2c()
pn532.SAMconfigure()

fields = [] 
rows = []

with open("students.csv", 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row)
        
            

while True:
    print("Make the child stand on the scale till the blinking line stops blinking... \n")
    print("Once the line stops blinking hold the Height scanner parallel to the ground using the inbuilt spirit level. \n")
    print("When the scanner is in position swipe the nfc card on the nfc module \n")
    nfc_id = pn532.read_mifare().get_data()
    nfc_id = [hex(p) for p in nfc_id]    
    id = nfc_id[7] + nfc_id[8] + nfc_id[9] + nfc_id[10]
    id = id.replace('0x', '')
    nfc_id = id
    for row in rows:
        if row[0] == nfc_id:
            print(nfc_id)
            save_json(row[2],row[3])
            time.sleep(0.5) 
            my_file = Path("scaleData.json")
            if my_file.is_file():
                with open('scaleData.json') as json_file:
                    data = json.load(json_file)
                    data2 = {
                        "Student_Id" : nfc_id,
                        "Body_metrics" : data
                   }
                    sendToCloud(data2)
                    os.remove("scaleData.json")
                    print("Data entry successful \n")
                    


