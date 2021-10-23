# adding noises on 5-worst and epslack 
# written by mgwoo (10/19/2021)
import json
import numpy as np 
import copy
import sys
from functools import cmp_to_key

def SortWns(a, b):
  na = float(a[0])
  nb = float(b[0])

  if na > 0:
    if nb > 0:
      return (na - nb)
    else:
      return True
  else:
    if nb > 0:
      return False
    else:
      return (na - nb)

np.random.seed(777)
design = sys.argv[1] 
# design will be "dir1/dir2/dir3/..../aes_cipher_top_1", etc.

maxError = 0.02
targetError = 0.02

def GetRandVal(targetError, maxError):
  randVal = np.random.normal(1.0, targetError/2.0)
  while abs(randVal-1.0) >= maxError:
    randVal = np.random.normal(1.0, targetError/2.0)
  # print("RAND:", randVal)
  return randVal
    

f = open("%s_endpoint_slacks.json" % (design), 'r') 
cont = f.read()
f.close()

arr = json.loads(cont)
epOrigSlackDict = dict()
epNewSlackDict = dict()

for ep, epSlack in zip(arr['pins'], arr['slacks']):
  epOrigSlackDict[ep] = float(epSlack)

slacks = []
# for epSlack in arr['slacks']:
for epSlack, pin in zip(arr['slacks'], arr['pins']):
  randVal = GetRandVal( targetError, maxError )
  slacks.append("%.3f" % (float(epSlack) * randVal))
  # print(pin, epSlack)

arr['slacks'] = slacks

# write noised epslack JSON
f = open("%s_endpoint_slacks.noise.json" % (design), 'w')
f.write(json.dumps(arr, indent=2))
f.close()

f = open("%s_5_worst.json" % (design), 'r')
cont = f.read()
f.close()

arr = json.loads(cont)
newCont = copy.deepcopy(arr)
print(arr['summary'])

for top in ["top%d" % (i) for i in range(1,6)]:
  topKArr = arr['detail'][top]
  totalRAT = float(topKArr['pathRAT'])
  totalAAT = float(topKArr['pathAAT']) 
  slack = float(topKArr['slack'])
  cp = float(topKArr['clockPeriod'])
  setupTime = float(topKArr['setupTime'])
  
  aatNoise = [GetRandVal(targetError, maxError) for _ in range(len(topKArr['pathList']))]
  ratNoise = [GetRandVal(targetError, maxError) for _ in range(len(topKArr['clockPathList']))]

  accmAAT = 0
  newAATPathArr = []
  for idx, (path, noise) in enumerate(zip(topKArr['pathList'], aatNoise)):
    if path['delay'] == "":
      newAATPathArr.append(path)
      continue
    
    # new delay calc
    newDelay = round(float(path['delay']) * noise,3)
    accmAAT += newDelay

    # save into new Array
    newPath = copy.deepcopy(path)
    newPath['delay'] = "%.03f" % (newDelay)
    newPath['AAT'] = "%.03f" % (accmAAT)
    newAATPathArr.append(newPath)

  newAAT = round(accmAAT,3)


  print("%s Path Noise" %(top))
  print("AAT", totalAAT, "->", newAAT)

  accmRAT = 0
  newRATPathArr = []
  for idx, (clkPath, noise) in enumerate(zip(topKArr['clockPathList'], ratNoise)):
    if clkPath['delay'] == "":
      newRATPathArr.append(clkPath)
      continue

    newDelay = round(float(clkPath['delay']) * noise,3)
    accmRAT += newDelay

    # save into new Array
    newPath = copy.deepcopy(clkPath)
    newPath['delay'] = "%.03f" % (newDelay)
    newPath['AAT'] = "%.03f" % (accmRAT)
    newRATPathArr.append(newPath)

  newRAT = round(cp + accmRAT - setupTime,3)
  print("RAT", totalRAT, "->", newRAT)

  newSlack = round(newRAT - newAAT, 3)
  print("Slack", slack, "->", newSlack) 

  # update newCont JSON
  newCont['detail'][top]['pathList'] = newAATPathArr
  newCont['detail'][top]['clockPathList'] = newRATPathArr
  newCont['detail'][top]['pathRAT'] = "%.03f" % (newRAT)
  newCont['detail'][top]['pathAAT'] = "%.03f" % (newAAT)
  newCont['detail'][top]['slack'] = "%.03f" % (newSlack)
  
  print("")

# sort again by slack,  increasing order
tmpList = [[val['slack'], val] for key,val in newCont['detail'].items()]
tmpList = sorted(tmpList, key=cmp_to_key(SortWns))

# rewrite newcont JSON with updated order
for idx, topK in enumerate(tmpList):
  newCont['detail']["top%d" % (idx+1)] = topK[1]
  print("Sorted Top%d Slack:" % (idx+1), topK[0])

# update WNS
newCont['summary']['WNS'] = newCont['detail']['top1']['slack']

# write noised 5-worst JSON
f = open("%s_5_worst.noise.json" % (design), 'w')
f.write(json.dumps(newCont, indent=2))
f.close()


