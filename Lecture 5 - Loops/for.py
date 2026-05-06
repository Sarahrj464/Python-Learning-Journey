# for loop --- traversing list, tuple, string

values = [1,2,3,4,5]
for num in values:
  print(num)
  

fruits = ["orange","kiwi","cherry","lechi"]
for i in fruits:
  print(i)
  
  
  
name="Sarah"
for n in name:
  if(n=='r'):
    print("char found")
    break
  print(n)
else:   # does not execute in case of break
  print("end")
  


# print 1-10
for i in range(1,11):
  print(i)
  
  
  
# print even num
for x in range(1,21):
  if(x%2==0):
    print(x)