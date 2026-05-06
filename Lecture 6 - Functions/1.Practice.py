# print len of list
fruits = ["orange","kiwi","cherry","grapes","lemon"]
def printLen(list):
  print(len(list))
  
printLen(fruits)
printLen("Ali")
printLen("Zariyun")


# print elements in single line
print(fruits[0],end=" ")
print(fruits[1],end=" ")
print(fruits[2],end=" ")
print(fruits[3],end=" ")
print(fruits[4],end=" ")




def printSingle(myList):
  for items in myList:
    print(items,end=" ")
  
printSingle(fruits)
print()




# find factorial
def findFact(n):
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  return fact
  
f=findFact(5)
print("Factorial:",f)



# convert usd to pkr
# method 1
def convertPK(n):
  usd = 279.25
  pk=n*usd
  return pk

currency = convertPK(1)
print(currency)



# method 2
def converter(val):
  usd=279.5
  print(val,"USD =",usd*val,"PKR")
  
converter(200)



# method 3
def converter(val):
  usd=279.5
  pkr=val*usd
  return pkr
  
mycurrency=converter(200)
print(mycurrency,"PKR")



# n=int(input("Enter number"))
# if(n%2==0):
#   print("even")
# else:
#   print("odd")
  
  
# take num as input and check it is even or odd
def num(n):
  if(n%2==0):
    print("even")
  else:
    print("odd")
  
# num(23)
x=int(input("Enter number: "))
num(x)