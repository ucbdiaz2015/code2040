import requests
import json

payload1 = {"token":"5ZLE6uPAvA"}
r1 = requests.post("http://challenge.code2040.org/api/status", json=payload1)

print r1.text