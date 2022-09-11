a = int(input("Enter number : "))
s = 2
for i in range(a):
  x = a
  time = 1
  for j in range(s):
    print(" "*x,end="")
    print("*"*time,end="")
    x -=1
    time +=2
    print("")
  s += 1
print(" "*a+"|")
print("="*a+"V"+"="*a)