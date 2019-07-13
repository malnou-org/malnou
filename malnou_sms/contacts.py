import re

contacts_list = []

def isValid(s): 
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
    return Pattern.match(s) 

def contacts(countryCode):
    with open('Contacts.txt') as cf:
        for line in cf:
            line = str(line)
            line = line.strip('\n')
            if (isValid(line)):
                if (len(line) == 10):
                    line = countryCode + line
                contacts_list.append(line)
    return contacts_list
