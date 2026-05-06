# # Level 3 — Lists

# # Q8.
# # Create a list of 5 numbers and print:

# # the sum
# # the largest number

# list = [2,5,8,6,3]
# s=0
# for i in list:
#   s=s+i
# print("Sum:",s)

# # print largest num
# list1 = [3,5,7,9,2]
# largest = list1[0]
# for val in list1:
#   if (val>largest):
#     largest=val
# print(largest)


# # Q9.
# # Write a program to remove duplicates from a list.

# # Example
# # Input: [1,2,2,3,4,4,5]
# # Output: [1,2,3,4,5]


# mylist = [1,2,2,3,4,4,5]
# new_list=set(mylist)
# print(new_list)



# # Q10.
# # Take 5 numbers from user and store them in a list, then print the average.

# list = []
# a=int(input("enter num 1: "))
# b=int(input("enter num 2: "))
# c=int(input("enter num 3: "))
# d=int(input("enter num 4: "))
# e=int(input("enter num 5: "))
# list.append(a)
# list.append(b)
# list.append(c)
# list.append(d)
# list.append(e)
# print(list)
# sum=a+b+c+d+e
# print(sum/5.0)





# Part 3: Lists & Tuples

# 11️⃣ Create a list of 5 numbers and print:

# largest number
# smallest number

list=[4,5,7,8,3]
largest=list[0]
smallest=list[0]
for n in list:
  if (n>largest):
    largest=n
  if (n<smallest):
    smallest=n
print(largest)
print(smallest)




# 12️⃣ Take 5 numbers from the user and store them in a list. Print the sum of all numbers.

list = []
sum=0
for i in range(1,6):
  n=int(input("Enter number: "))
  list.append(n)
  sum+=n
print("Sum:",sum)





# 13️⃣ Write a program to remove duplicates from a list.
# Example
# [1,2,2,3,4,4] → [1,2,3,4]

list=[1,2,2,3,4,4]
print(set(list))



# 14️⃣ Convert a list into a tuple.

list = [10,20,30,40]
print(tuple(list))




# 15️⃣ Check whether an element exists in a list or not.

myList=[1,2,3,4,5]
num=int(input("Enter a number: "))
if num in myList:
  print("element found")
else:
  print("element not found")
