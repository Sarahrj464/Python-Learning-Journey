# # Functions
# # Q1 — Basic
# # Write a function greet(name) that takes a name and prints "Hello, Sarah!"

# def greet(name):
#   print(f"Hello {name}")
  
# myName=input("Enter your name: ")
# greet(myName)



# # Q2 — Return Value
# # Write a function add(a, b) that takes two numbers and returns their sum.


# def add(a,b):
#   return (a+b)
# sum=add(2,3)
# print("Sum is:",sum)


# # Q3 — Default Parameter
# # Write a function power(num, exp=2) that returns num to the power of exp. If no exp given, square the number by default.

# # power(3) → 9
# # power(3, 3) → 27

# def power(num, exp=2):
#   return (num**exp)
# pow1=power(3)
# pow2=power(3,3)
# print("Power:",pow1)
# print("Power:",pow2)




# # Q4 — Real Use
# # Write a function is_even(n) that returns True if number is even, False if odd.

# def is_even(n):
#   if(n%2==0):
#     return True
#   else:
#     return False

# num=int(input("Enter number: "))
# show=is_even(num)
# print(show)



# Q5 — List + Function
# Write a function find_max(numbers) that takes a list and returns the largest number — without using max().


# find largest num 
def find_Max(num):
  largest_num=num[0]
  for n in num:
    if(n>largest_num):
      largest_num=n
  return largest_num

list=[2,8,6,9,3]
largest=find_Max(list)
print("Largest num:",largest)




# find index
def findIdx(n):
  largest_index=0
  for i in range(len(n)):
    if(n[i]>n[largest_index]):
      largest_index=i
  return largest_index

mylist=[2,8,6,9,3]
largestidx=findIdx(mylist)
print("Largest index:",largestidx)