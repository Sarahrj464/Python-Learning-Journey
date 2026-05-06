# # # Level 6 — Functions

# # # Q16.
# # # Write a function that returns the square of a number.

# def square(n):
#   return n*n
# sq=square(5)
# print("square is:",sq)


# # # Q17.
# # # Write a function that checks whether a number is prime.  2,3,5,7,11,13,17

# # # without function
# n=5
# is_Prime=True
# for i in range(2,n):
#   if(n%i==0):
#     is_Prime=False
#     break
# print(is_Prime)
  


# # # with function
# def check(n):
#   isPrime=True
#   for i in range(2,n):
#     if (n%i==0):
#       isPrime=False
#       break
#   return isPrime
# result = check(110)
# print(result)
    



# # # Q18.
# # # Write a function that counts vowels in a string.

# string = "hello"
# vowels="aeiou"
# count=0
# for char in string:
#   if char in vowels:
#     count=count+1
# print(count)


# # # with function
# vowels="aeiou"
# def checkVowels(name):
#   c=0
#   for char in name:
#     if char in vowels:
#       c=c+1
#   return c
# myString=input("Enter a string: ")
# result=checkVowels(myString)
# print("Vowels in string:",result)





# # Q19.
# # Write a program that:
# # takes a list of numbers
# # returns even numbers only using a function
# # Example

# # Input: [1,2,3,4,5,6]
# # Output: [2,4,6]

# list = []
# def even(mylist):
#   evenNum = []
#   for n in mylist:
#     if (n%2==0):
#       evenNum.append(n)
#   return evenNum
  
# for i in range(1,6):
#   num=int(input("enter number: "))
#   list.append(num)
# result=even(list)
# print(result)


# Part 6: Functions & Recursion

# 26️⃣ Write a function to check even or odd number.

def check(n):
  if(n%2==0):
    print("even")
  else:
    print("odd")
    
num=int(input("enter number: "))
check(num)



# 27️⃣ Write a function to find maximum of three numbers.

def findMax(a,b,c):
  if (a>b):
    if(a>c):
      print("a is largest")
    else:
      print("c is largest")
  else:
    if(b>c):
      print("b is largest")
    else:
      print("c is largest")
findMax(3,5,2)




# 28️⃣ Write a recursive function to calculate factorial.

def factorial(n):
  if n==0 or n==1:
    return 1
  return factorial(n-1)*n

num=int(input("Enter number: "))
result=factorial(num)
print(result)



# 29️⃣ Write a function that returns sum of elements of a list.

def sum(n):
  s=0
  for el in n:
    s+=el
  return s
  
list=[10,20,30,40,50]
totalSum=sum(list)
print("Sum:",totalSum)




# 30️⃣ Write a function that counts vowels in a string.

def show(n):
  vowels="aeiou"
  count=0
  for el in n:
    if el in vowels:
      count+=1
  return count
  
string="Sarah"
r=show(string)
print(r)