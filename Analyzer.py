import requests    
import json
import time
import hashlib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

def comp(e):
	a = e.keys()
	if 'rating' in a :
		return e['rating']
	return 10000
current_time = str(int(time.time()))


#INPUT
handles = ["tourist"]
#keys
key = {}
secret = {}
need = {}

for x in handles:
	need.update({x : 0})

need.update({"tourist" : 0})
key.update({"tourist" : ""})
secret.update({"tourist" : ""})
#/INPUT



problems = {}

probs = 0

for x in handles:
    if need[x] == 1:
    	reque = "https://codeforces.com/api/user.status?handle=" + x + "&lang=en"
    	reque += "&apiKey=" + key[x] + "&time=" + (current_time)
    	reque += "&apiSig=123456"
    	hsh = "123456/user.status?apiKey=" + key[x] + "&handle=" + x + "&lang=en" + "&time=" + current_time + "#" + secret[x]
    	reque += hashlib.sha512(hsh.encode('utf-8')).hexdigest()
    	r = requests.get(reque)
    else:	
    	r = requests.get("https://codeforces.com/api/user.status?lang=en&handle=" + x)		
    time.sleep(0.3)
    data = json.loads(r.text)
    status = data['result']
    print(x + " " + data['status'])
    for submission in status :
    	if submission['verdict'] == 'OK' :
    		info = submission['problem'].keys()
    		name = 'Unknown'
    		if 'name' in info:
    			name = submission['problem']['name']
    		rating = 0
    		if 'rating' in info:
    			rating = submission['problem']['rating']
    		if not (name in problems):
    			problems.update({name + ":" + str(rating) : rating})


req = ratingcnt = {}
names = problems.keys()

for j in range(800, 3400, 100):
	ratingcnt.update({j : 0})

for key in names:
	if(problems[key] in ratingcnt):
		ratingcnt[problems[key]] += 1
	else:
		ratingcnt.update({problems[key] : 1})

#print("Unrated" + ":" + str(ratingcnt[0])) 

groups = []
counts = []

for j in range(800, 3400, 100):
	groups.append(str(j))
	counts.append(ratingcnt[j])
#	print(str(j) + ":" + str(ratingcnt[j]))

f = plt.figure()
f.set_figwidth(22)
#f.set_figheight(10)
plt.bar(groups, counts)

#plt.show()
plt.savefig('my graph', dpi=100)

#print(len(problems))