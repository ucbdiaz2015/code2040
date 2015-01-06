import requests

payload1 = {"token":"5ZLE6uPAvA"}
r1 = requests.post("http://challenge.code2040.org/api/getstring", json=payload1)

str = r1.text
print str

index = len(str)-4
string = ""
for i in range(len(str)-14):
	string+=str[index]
	index -= 1

print string

payload2 = {"token":"5ZLE6uPAvA","string":string}
r2 = requests.post("http://challenge.code2040.org/api/validatestring", json=payload2)

print r2.text


	