# # Level 1 — Basic (Variables, Input, Conditions)

# # Q1.
# # Write a program that takes a number from the user and prints whether it is even or odd.
# n=int(input("Enter number: "))
# if(n%2==0):
#   print("even")
# else:
#   print("odd")



# # Q2.
# # Take two numbers as input and print the largest number.
# a=int(input("Enter number 1: "))
# b=int(input("Enter number 2: "))
# if(a>b):
#   print(a,"is largest")
# else:
#   print(b,"is largest")




# # Q3.
# # Take a student's marks and print:

# # A if marks ≥ 80
# # B if marks ≥ 60
# # C if marks ≥ 40
# # Fail if marks < 40
# marks=int(input("Enter student marks: "))
# if (marks>=80) and (marks<=100):
#   print("A")
# elif (marks>=60) and (marks<80):
#   print("B")
# elif (marks>=40) and (marks<60):
#   print("C")
# else:
#   print("F")





# # Q4.
# # Write a program that asks the user for age and checks if the person is eligible to vote (age ≥ 18).
# age=int(input("Enter age: "))
# if age>=18:
#   print("eligible to vote")
# else:
#   print("not eligible to vote")



# Part 1: Variables & Data Types

# 1️⃣ Take two numbers from the user and print their sum, difference, multiplication, and division.

a=int(input("Enter number: "))
b=int(input("Enter number: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)





# 2️⃣ Take a number from the user and print:

# its square
# its cube

n=int(input("Enter number: "))
print("Square: ",n*n)
print("Cube",n*n*n)








# 3️⃣ Write a program to swap two variables without using a third variable.

x=10
y=5
x,y=y,x
print(x,y)







# 4️⃣ Take a float number from the user and convert it into integer type.

num=float(input("Enter number: "))
print(int(num))



# 5️⃣ Write a program to check the data type of the following:

# 10
# 3.14
# "Python"
# True

a1=10
b1=3.14
c1="string"
d1=True
print(type(a1))
print(type(b1))
print(type(c1))
print(type(d1))