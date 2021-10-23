# adding noises on IR drop
# written by mgwoo (10/19/2021)
import json
import numpy as np 
import sys

np.random.seed(777)
design = sys.argv[1] 
# design will be "dir1/dir2/dir3/..../aes_cipher_top_1", etc.

maxError = 0.02
targetError = 0.01
precision = 5

def GetRandVal(targetError, maxError):
  randVal = np.random.normal(1.0, targetError)
  while abs(randVal-1.0) >= maxError:
    randVal = np.random.normal(1.0, targetError)
  # print("RAND:", randVal)
  return randVal
    

f = open("%s_ir.VDD.json" % (design), 'r') 
cont = f.read()
f.close()

arr = json.loads(cont)
VDD = arr['summary']['vdd']

newList = []

for inst, vol in zip(arr['detail']['instanceList'], arr['detail']['voltages']):
  voltage = (VDD - vol) * GetRandVal( targetError, maxError ) 
  newList.append([inst, VDD - voltage])

newList.sort(key=lambda x: x[1])
arr['detail']['instanceList'] = [l[0] for l in newList]
arr['detail']['voltages'] = [round(l[1],precision) for l in newList]

arr['summary']['wir']['instanceName'] = newList[0][0]
arr['summary']['wir']['ir'] = round(VDD - newList[0][1], precision)
arr['summary']['wir']['voltage'] = round(newList[0][1], precision)

# write noised 5-worst JSON
f = open("%s_ir.VDD.noise.json" % (design), 'w')
f.write(json.dumps(arr, indent=2))
f.close()

print("%s_ir.VDD.noise.json is generated" % (design))


f = open("%s_ir.VSS.json" % (design), 'r') 
cont = f.read()
f.close()

arr = json.loads(cont)

newList = []

for inst, vol in zip(arr['detail']['instanceList'], arr['detail']['voltages']):
  voltage = vol * GetRandVal( targetError, maxError ) 
  newList.append([inst, voltage])

newList.sort(key=lambda x: x[1])
arr['detail']['instanceList'] = [l[0] for l in newList]
arr['detail']['voltages'] = [round(l[1],precision) for l in newList]

arr['summary']['wir']['instanceName'] = newList[-1][0]
arr['summary']['wir']['ir'] = round(newList[-1][1], precision)
arr['summary']['wir']['voltage'] = round(newList[-1][1], precision)

# write noised 5-worst JSON
f = open("%s_ir.VSS.noise.json" % (design), 'w')
f.write(json.dumps(arr, indent=2))
f.close()

print("%s_ir.VSS.noise.json is generated" % (design))
