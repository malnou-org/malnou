import os
import subprocess

mac_present = False
subprocess.check_output(['bash','-c', 'chmod +x  le.sh'])
subprocess.check_output(['bash','-c', './le.sh'])

text_file = open("result.txt", "r")
lines = text_file.readlines()
for line in lines:
	if 'MIBCS' in line:
		mac_address = line.split()[0]
		text_file2 = open("config.txt", "w")
		text_file2.write(mac_address)
		mac_present = True

if mac_present:
	print("Setup was successful")
else:
	print("Setup Unsuccessful!")
	print("No scale found")
	print("Step on the scale to wake it from sleep and try the setup again")


os.remove("result.txt")
