#  Basic Class & Object
# Create a class Car with attributes brand, model, year. Create 2 objects and print their details.

class Car:
  def __init__(self,brand,model,year):
    self.brand=brand
    self.model=model
    self.year=year
    
c1=Car("Audi","A3",2026)
print(c1.brand)
print(c1.model)
print(c1.year)
c2=Car("BMW","3-Series",2025)
print(c2.brand)
print(c2.model)
print(c2.year)


# Constructor
# Create a class Student with a parameterized constructor that takes name and marks. Print student details using a method show().

class Student:
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
  
  def show(self):
    print("Hello",self.name,"This is your marks:",self.marks)

s1=Student("Sarah",87)
s1.show()






#  Class vs Instance Attribute
# Create a class Bank with:

# class attribute: bank_name = "HBL"
# instance attributes: account_holder, balance
# Create 2 objects and print both class and instance attributes.

class Bank:
  bank_name = "HBL"
  def __init__(self,acc,bal):
    self.account_holder=acc
    self.balance=bal
    
b1=Bank("siblings",10000)
print(Bank.bank_name)
print(b1.account_holder)
print(b1.balance)

b2=Bank("employee",5000)
print(b2.bank_name)
print(b2.account_holder)
print(b2.balance)



# Method
# Create a class Calculator with methods:

# add(a, b)
# subtract(a, b)
# multiply(a, b)
# Create an object and use all methods.

class Calculator:
  def __init__(self,num1,num2):
    self.first=num1
    self.second=num2
    
  def add(self):
    sum=self.first+self.second
    print("Sum:",sum)
    
  def subtract(self):
    sub=self.first-self.second
    print("Subtract:",sub)
    
  def multiply(self):
    mul=self.first*self.second
    print("Multiply:",mul)

c1=Calculator(10,5)
c1.add()
c1.subtract()
c1.multiply()


# Static Method
# Create a class MathHelper with a static method square(n) that returns square of a number. Call it without creating an object.

class MathHelper:
    
  @staticmethod
  def square(n):
    return n*n
  
print(MathHelper.square(5))