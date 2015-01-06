import requests
import json

payload1 = {"token":"5ZLE6uPAvA"}
r1 = requests.post("http://challenge.code2040.org/api/haystack", json=payload1)

json_data = json.loads(r1.text)


needle = json_data["result"]["needle"]
print needle

index = json_data["result"]["haystack"].index(needle)
print index

payload2 = {"token":"5ZLE6uPAvA", "needle":index}
r2 = requests.post("http://challenge.code2040.org/api/validateneedle", json=payload2)
print r2.text