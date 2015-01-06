imoprt requests
payload= {"email":"ucbdiaz2015@berkeley.edu","github":"https://github.com/ucbdiaz2015/code2040"}
r = requests.post("http://challenge.code2040.org/api/register", json=payload)
print r.text

#u’{“result":"5ZLE6uPAvA"}\n'