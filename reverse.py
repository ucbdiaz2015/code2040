import requests
import json

payload1 = {"token":"5ZLE6uPAvA"}
r1 = requests.post("http://challenge.code2040.org/api/getstring", json=payload1)

str = r1.text
print str
json_data = json.loads(r1.text)["result"] #obtain response

print json_data

index = len(json_data)-1
string = ""
for i in range(len(json_data)):
	string+=json_data[index]
	index -= 1
#string = json_data[::-1] is a simpler way of reversing (http://stackoverflow.com/questions/931092/reverse-a-string-in-python)

print string
payload2 = {"token":"5ZLE6uPAvA","string":string}
r2 = requests.post("http://challenge.code2040.org/api/validatestring", json=payload2)

print r2.text


	