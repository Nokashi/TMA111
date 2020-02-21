import time
import random

def maxCars(x):
  maxX = max(x)
  maxList = []
  for i in range(len(x)):
    if x[i] == maxX:
      maxList.append(i)
  rand1 = random.choice(maxList)
  return rand1


f1 = random.randint(0,10)
f2 = random.randint(0,10)
f3 = random.randint(0,10)
trafficLights = [f1,f2,f3]
while True:
  status = ""
  time.sleep(2)
  max1 = maxCars(trafficLights)
  for i in range(len(trafficLights)):
    if i == max1:
      rand = min(trafficLights[i],random.randint(5,10))
      trafficLights[i] -= rand
      status += str(rand) + " cars left from traffic light " + str(i + 1) + "\n" + "It has " + str(trafficLights[i]) + " cars \n\n"
    else:
      rand = random.randint(0,5)
      trafficLights[i] += rand
      status += str(rand) + " cars arrived at traffic light " + str(i+1) + "\n" + "It has " + str(trafficLights[i]) + " cars \n\n"
  print(status)
  print("--------------------------------------------------")
  
