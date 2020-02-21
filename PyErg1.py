def sortWords(x,y): 
  l = len(x)  
  for i in range(l): 
    for j in range(0, l-i-1): 
      if x[j] < x[j+1] : 
        temp1 = x[j]
        x[j] = x[j+1]
        x[j+1] = temp1
        temp2 = y[j]
        y[j] = y[j+1]
        y[j+1] = temp2
  

def switch(x):
  reversedWord = ""
  for i in range(len(x) - 1,-1,-1):
    if x[i] not in "aeiou":
      reversedWord += x[i]
  return reversedWord
      


f = input("give me the file name \n \t")
f = open(f,"r").read()
if f[-1] == " ":
  f = f[0:-1]
wordList = f.split(" ")
wordLength = []
for i in wordList:
  wordLength.append(len(i))
sortWords(wordLength,wordList)
top5 = wordList[0:5]
for i in top5:
  print(switch(i))
