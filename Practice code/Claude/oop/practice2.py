# Q1 — Inheritance
# Create a class Animal with method speak(). Create two child classes Dog and Cat that override speak() with their own sounds.

class Animal:
  def speak(self):
    print("Animal speak")

class Dog(Animal):
  def speak(self):
    print("Waoo")
  
class Cat(Animal):
  def speak(self):
    print("Meaow")
  
c1=Cat()
c1.speak()



# Q2 — super()
# Create a class Person with constructor taking name and age. Create a child class Teacher that adds subject. Use super() to call parent constructor.

class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

class Teacher(Person):
  def __init__(self,name,age,sub):
    super().__init__(name,age)
    self.sub=sub
    
t1=Teacher("Sarah",22,"Math")
print(t1.name)
print(t1.age)



# Q3 — Class Method
# Create a class Counter with a class attribute count = 0. Every time an object is created, count increases by 1. Use @classmethod to print total count.


class Counter:
  count=0
  
  def __init__(self):
    Counter.count+=1
  
  @classmethod
  def show(cls):
    print(cls.count)
  
c1=Counter()
c2=Counter()
c3=Counter()
Counter.show()



# Q4 — Polymorphism
# Create a class Shape with method area(). Create two child classes Circle and Rectangle that override area() with their own formula.


class Shape:
  def area():
    pass
    
class Circle(Shape):
  def __init__(self,radius):
    self.radius=radius
    
  def area(self):
    return 3.14*self.radius*self.radius

class Rectangle(Shape):
  def __init__(self,len,width):
    self.len=len
    self.width=width
    
  def area(self):
    return self.len*self.width
  
r1=Rectangle(2,3)
print(r1.area())
  



# Q5 — Operator Overloading
# Create a class Point with x and y. Overload + operator to add two points together.

# Example: Point(1,2) + Point(3,4) → Point(4,6)


class Point:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
  def show(self):
    print("Point (",self.x,",",self.y,")")
    
  def __add__(self,z):
    newX=self.x+z.x
    newY=self.y+z.y
    return Point(newX,newY)
  
p1=Point(1,2)
p1.show()
p2=Point(3,4)
p2.show()

p3=p1+p2
p3.show()


# Q1 — super()
# Create a class Vehicle with constructor taking brand and speed. Create child class Car that adds num_doors. Use super().

class Vehicle:
  def __init__(self,brand,speed):
    self.brand=brand
    self.speed=speed
    
class Car(Vehicle):
  def __init__(self,brand,speed,num_doors):
    self.num_doors=num_doors
    super().__init__(brand,speed)

c1=Car("Fortuner","200 KM/H",10)
print(c1.brand)
print(c1.speed)
print(c1.num_doors)






# Q2 — super() + method
# Create class Animal with method info() that prints name. Create child class Dog that overrides info() but also calls parent's info() using super().

class Animal:
  def info(self):
    print("Tony")

class Dog(Animal):
  @property
  def info(self):
    super().info()   # call parent info -- Tony
    print("Stark")
    
d1=Dog()
print(d1.info)




# Q3 — @property
# Create class Rectangle with length and width. Add a @property method area that returns length × width. Access it without ().

class Rectangle:
  def __init__(self,length,width):
    self.length=length
    self.width=width
    
  @property
  def area(self):
    return self.length*self.width
  
r1=Rectangle(2,3)
print(r1.area)



# Q4 — @classmethod
# Create class Student with class attribute school = "City School". Add @classmethod method change_school(cls, name) that updates school name. Print before and after change.


class Student:
  school = "City School"
  
  @classmethod
  def change_school(cls,name):
    cls.name=name

s1=Student()
print(s1.school)
Student.school="DPS School"
print(Student.school)




# Q5 — Mixed
# Create class Employee with:

# constructor: name, salary
# @property: annual_salary — returns salary × 12
# @classmethod: company_name — prints company name

class Employee:
  def __init__(self,name,sal):
    self.name=name
    self.sal=sal
    
  @property
  def annual_salary(self):
    return self.sal*12
  
  @classmethod
  def company_name(cls,c_name):
    print(f"Company: {c_name}")
    
e1=Employee("Sarah",5000)
print(e1.name)
print(e1.annual_salary)
e1.company_name("10Pearls")


# Try karo! 💪 Sonnet 4.6





# Q1 — Inheritance + super()
# Create class Phone with brand and price. Child class Smartphone adds os. Use super() and print all details.

class Phone:
  def __init__(self,brand,price):
    self.brand=brand
    self.price=price

class Smartphone(Phone):
  def __init__(self,brand,price,os):
    super().__init__(brand,price)
    self.os=os
    
sp=Smartphone("Techno",45000,"Android")
print(sp.os)
print(sp.brand)
print(sp.price)





# Q2 — Hierarchical Inheritance
# Create class Shape with method draw(). Create 3 child classes Circle, Square, Triangle — each overrides draw() with their own message.


class Shape:
  def draw(self):
    print("draw shape")

class Circle(Shape):
   def draw(self):
    print("draw circle")

class Square(Shape):
   def draw(self):
    print("draw square")
  
class Triangle(Shape):
   def draw(self):
    print("draw triangle")
    
t1=Triangle()
t1.draw()




# Q3 — @property
# Create class Student with name and marks. Add @property method grade that returns:

# A if marks >= 80
# B if marks >= 60
# C if marks >= 40
# Fail otherwise

class Student:
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
    
  @property
  def grade(self):
    if (self.marks>=80):
      return "A"
    elif (self.marks>=60):
      return "B"
    elif (self.marks>=40):
      return "C"
    else:
      return "F"
      
st=Student("Sarah",76)
print(st.name)
print(st.grade)




# Q4 — @classmethod
# Create class Bank with class attribute interest_rate = 5. Add @classmethod to update interest rate. Create 2 objects — show that rate changed for both.


class Bank:
  interest_rate = 5
  
  @classmethod
  def change_rate(cls,new_rate):
    cls.interest_rate=new_rate
    
b1=Bank()
b2=Bank()
print(b1.interest_rate)
print(b2.interest_rate)
Bank.change_rate(10)
print(b1.interest_rate)
print(b2.interest_rate)






# Q5 — Polymorphism
# Create class Animal with method sound(). Create child classes Dog, Cat, Cow — each overrides sound(). Make a list of all 3 objects and call sound() on each using a loop.

class Animal:
  def sound(self):
    print("animal sound")
    
class Dog(Animal):
  def sound(self):
    print("dog sound")
  
class Cat(Animal):
  def sound(self):
    print("cat sound")
  
class Cow(Animal):
  def sound(self):
    print("cow sound")
    
animals=[Dog(),Cat(),Cow()]
for animal in animals:
  animal.sound()