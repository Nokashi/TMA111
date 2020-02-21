def check(x):
  x = int(x)
  x *= 3
  x += 1
  sum = 0
  for i in str(x):
    sum += int(i)
  if len(str(sum)) == 1:
    print("The first one digit number is " + str(sum))
  else:
    check(sum)

check(input("Give me a number: "))