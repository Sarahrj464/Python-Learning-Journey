# # Conditions
# Take a number — print whether it is positive, negative, or zero
n=int(input("Enter a number: "))
if(n>0):
  print("positive")
elif(n<0):
  print("negative")
else:
  print("zero")



# Take an age — print "minor" if less than 18, "adult" if 18 or above
age=int(input("Enter your age: "))
if(age<18):
  print("minor")
else:
  print("adult")
  
  
# Find the largest number among three numbers
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))
if(a>b):
  if(a>c):
    print("a is largest")
  else:
    print("c is largest")
else:
  if(b>c):
    print("b is largest")
  else:
    print("c is largest")