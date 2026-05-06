# lists are just like arrays used to store set of values
# difference:
# array --> store data of same data type
# list --> store data of differ data types
# lists are built-in data type 
# lists contain square brackets

marks=[23.4,56.7,78.7,98.0]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[3])


# strings in python ---> immutable (not change)
# lists in python ---> mutable

# values can be only be accessed from given index
student=["Sarah",34.5,"Pakistan"]    # 3 indexes
print(student)
print(student[1])
student[0]="Amirah"
print(student)
# print(student[4])  --> not possible bcz index size is 3


str = "Hello"
print(str)
# str[0]="M"  ----> not possible to change any character of string
print(str)



# convert a list into set
myList = [23,45,67,89,90]
new_myList = set(myList)
print(new_myList)