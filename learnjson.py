#!/usr/bin/env python3

import json

data = {
  	'name' : 'ACME',
	'shares': 100,
	'price':542.23
}

#Encode Python Dictionary Data Structure to JSON String
json_str = json.dumps(data) 

#Decode JSON string back to Python Dictionary 
data = json.loads(json_str)

#Writing JSON data to file
with open('data.json','w') as f:
	json.dump(data,f)

#Reading data back
with open('data.json','r') as f:
	data = json.load(f)

print(data)
