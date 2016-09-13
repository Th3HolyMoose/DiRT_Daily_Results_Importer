import sys
import json
import requests
import datetime
import os

dnow = datetime.datetime.utcnow().date()
dnow = (datetime.datetime.utcnow() - datetime.timedelta(hours=10, days=7)).date()



eventDate = dnow.strftime("%Y-%m-%d")
print eventDate

#raw_input("")

eventId = -1
test = requests.get("https://www.dirtgame.com/uk/events").text
nl = False
for line in test.split("\n"):
    if line.startswith('<select data-ng-model="eventId" id="weekly_prevEvents" name="weekly_prevEvents'):
        #eventId = line[(line.find('<option value="') + 15):(line.find('">Current event</option>'))]
        nl = True
        continue
    if nl == True:        
        eventId = line[(line.find('<option value="') + 15):(15 + line[15:].find('">'))]
        break

if eventId == -1:
    print "Could not find the weekly 1!"
    sys.exit()

os.system("python importEvent.py " + str(eventId) + " " + eventDate + " " + "weekly1")
print "Weekly 1: " + str(eventId)


#

eventId = -1
test = requests.get("https://www.dirtgame.com/uk/events").text
nl = False
for line in test.split("\n"):
    if line.startswith('<select data-ng-model="eventId" id="weekly2_prevEvents" name="weekly2_prevEvents'):
        #eventId = line[(line.find('<option value="') + 15):(line.find('">Current event</option>'))]
        nl = True
        continue
    if nl == True:        
        eventId = line[(line.find('<option value="') + 15):(15 + line[15:].find('">'))]
        break

if eventId == -1:
    print "Could not find the weekly 2!"
    sys.exit()

os.system("python importEvent.py " + str(eventId) + " " + eventDate + " " + "weekly2")
print "Weekly 2: " + str(eventId)
print "Weekly 1 & 2 imported"
