# using while loop -- list
num = [1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(num):
  print(num[i])
  i+=1
  
# while loop -- tuple
n = (1,4,9,16,25,36,49,64,81,100)
x=49
i=0
while i<len(n):
  if(n[i]==x):
    print("index found",i)
    print("value found",n[i])
    break
  i+=1
  print("end",i)    

  

# using for loop  --- list
for i in range(len(num)):
  print(num[i])
  

# print num from 1-100
for el in num:
  print(el)
  
  
  
# tuple
a=36
for i in range(len(n)):
  if(n[i]==a):
    print("value found at index:",i)
    break
  i+=1
  
  
# 2nd method
tup = (1,4,9,16,25,36,49,64,81,100)
x1=0
a1=25
for el in tup:
  if(el==a1):
    print("index found",x1)
  x1+=1