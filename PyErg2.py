f = input("give me the file name \n \t")
f = open(f,"r").read()
if f[-1] == " ":
  f = f[0:-1]
wordList = f.split(" ")
for i in wordList:
  countBad = 0
  countGood = 0
  for j in i:
    if j not in "aeiou":
      if j in "fckr":
        countBad += 1
      else:
        countGood += 1
  print( i + "\t Bad word") if countBad > countGood else print(i + "\t Good word")
  
