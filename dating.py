import requests
import json
import datetime

payload1 = {"token":"5ZLE6uPAvA"}
r1 = requests.post("http://challenge.code2040.org/api/time", json=payload1)


json_data = json.loads(r1.text)
print json_data

gdate = json_data["result"]["datestamp"]
interval = json_data["result"]["interval"]



givenDate = datetime.date(int(gdate[0:4]), int(gdate[5:7]), int(gdate[8:10]))
givenTime = datetime.time(int(gdate[11:13]), int(gdate[14:16], int(gdate[17:19])))

givenDateTime = datetime.datetime.combine(givenDate, givenTime) #timestamp
dateChange = datetime.timedelta(seconds=int(interval))			#interval into time
print dateChange
newDate = givenDateTime + dateChange							#updated
print str(newDate)

payload2 = {"token":"5ZLE6uPAvA", "datestamp":str(newDate)}
r2 = requests.post("http://challenge.code2040.org/api/validatetime", json=payload2)

print r2.text