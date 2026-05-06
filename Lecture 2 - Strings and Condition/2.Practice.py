# num is even or odd
num=int(input("Enter a number: "))
if(num%2==0):
  print(num,"is even")
else:
  print(num,"is odd")
  
  
  
# largest of 3 numbers --- Method 1
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if(a>b):
  if(a>c):
    print(a,"is greatest")
  else:
    if(c>b):
      print(c,"is greatest")
else:
  if(b>c):
    print(b,"is greatest")
  else:
    print(c,"is greatest")
    
  
  
# largest of 3 numbers --- Method 2
a1=int(input("Enter first number: "))
b1=int(input("Enter second number: "))
c1=int(input("Enter third number: "))
if(a1>=b1 and a1>=c1):
  print(a1,"is largest")
elif(b1>=c1):
  print(b1,"is largest")
else:
  print(c1,"is largest")  
  
  
  
  
# largest of 4 numbers 
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
d=int(input("Enter forth number: "))
if(a>=b and a>=c and a>=d):
  print(a,"is largest")
elif(b>=c and b>=d):
  print(b,"is largest")
elif(c>=d):
  print(c,"is largest")
else:
  print(d,"is largest")
  


  
# num is multiple of 7
# 7,14,21,28,35,42,...
n=int(input("enter a number: "))
if(n%7==0):
  print("multiple of 7")
else:
  print("not multiple of 7")