# # . Variables & Data Types

# # Write a Python program that takes temperature in Celsius from the user and converts it to Fahrenheit.

# C->F  F=9/5C+32
# F->C  C=5/9F-32

c=float(input("Enter temperature in Celcius: "))
f=9.0/5.0*c+32
print(f)


# # 2. Strings

# # Write a program that takes a string input from the user and counts the number of vowels (a, e, i, o, u) in the string.

string=input("Enter a string: ")
vowels="aeiou"
count=0
for char in string:
  if char in vowels:
    count+=1
print(count)





# # 3. Lists
# # Write a Python program that asks the user to enter 5 numbers, stores them in a list, and then prints:
# # the largest number
# # the smallest number
# # the average of all numbers

list = []
for i in range(1,6):
  n=int(input("Enter num: "))
  list.append(n)
largest=list[0]
smallest=list[0]
sum=0
for num in list:
  sum+=num
  if(num>largest):
    largest=num
  if(num<smallest):
    smallest=num
print("Largest:",largest)
print("Smallest:",smallest)
print("Average:",sum/len(list))
      

# 4. Tuple

# Create a list [10, 20, 30, 40, 50].
# Convert this list into a tuple and print the sum of all elements in the tuple.

mylist = [10, 20, 30, 40, 50]
tup=tuple(mylist)
sum=0
for i in tup:
  sum+=i
print("Sum:",sum)


# # 5. Dictionary
# # Create a dictionary that stores 3 students' names and their marks.
# # Write a program to find and print the student who has the highest marks.

students = {
    "Sarah": 90,
    "Amirah": 85,
    "Kashaf": 93
}
top_student=max(students,key=students.get)
print(top_student,students[top_student])


# # 6. Sets
# # Create two sets and write a program to display:
# # the union of the sets
# # the intersection of the sets

s1={1,2,3,4}
s2={2,3,5,6}
print(s1.union(s2))
print(s1.intersection(s2))



# # 7. Loops

# # Write a Python program that takes a number from the user and prints all of its factors.
# # Example:
# # For input 12 → Output: 1, 2, 3, 4, 6, 12

num=int(input("Enter number: "))
for i in range(1,num+1):
  if(num%i==0):
    print(i,end=" ")
print()
    
    
    
# # 8. Functions

# # Write a Python function that takes a list of numbers as input and returns the average of the numbers.

def avg(n):
  s=0
  for i in n:
    s+=i
  return s/len(n)
  
list=[1,2,3,4,5]
result=avg(list)
print("Average:",result)


# 9. File Handling

# Write a Python program that reads a text file and counts:
# the total number of lines
# the total number of words

with open("C:/Users/Home/Desktop/Python/gpt/read.txt","w") as f:
  f.write("Hello\nI am Sarah\nProgrammer and Developer")
  
# total words
with open("C:/Users/Home/Desktop/Python/gpt/read.txt","r") as f:
  data=f.read()
  words=data.split()
  print(len(words))
  
# total lines
def countLines():
  data=True
  line_no=0
  with open("C:/Users/Home/Desktop/Python/gpt/read.txt","r") as f:
    while True:
      data=f.readline()
      if not data:
        break
      line_no+=1
  print(line_no)
countLines()
  