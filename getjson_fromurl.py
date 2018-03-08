import json
import urllib.request

response = urllib.request.urlopen("http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input=Netflix")
s = response.read()
myList = (s.decode()) #byte to str
print(myList)
print(type(myList))
l = json.loads(myList) #str to dictionary
print(l)
print(type(l))
d = l[0]
print(type(d))

def get_json_response(myurl):
    with urllib.request.urlopen(myurl) as url:
        s = url.read() #byte
        print(s.decode()) #byte to str
        print(type(s.decode()))
        d = json.loads(s) #byte to dictionary
        print(d)
        print(type(d))

base_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="
myList = ['AAPL', 'MSFT']

for i in range(0,2):
    target_url = ('{0}{1}'.format(base_url , myList[i]))
    get_json_response(target_url)
