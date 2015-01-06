import requests
import json

payload1 = {"token":"5ZLE6uPAvA"}
r1 = requests.post("http://challenge.code2040.org/api/prefix", json=payload1)

print r1.text
json_data = json.loads(r1.text)

array = json_data["result"]["array"]
prefix = json_data["result"]["prefix"]
print prefix
print array
newArray = []
for i in array:
	if not i.startswith(prefix):	#only add items that dont start w/ prefix
		newArray.append(i)

print newArray

payload2 = {"token":"5ZLE6uPAvA", "array":newArray}
r2 = requests.post("http://challenge.code2040.org/api/validateprefix", json=payload2)
print r2.text