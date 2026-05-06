# # 🔹 Basic OOP Practice Questions

# ### 1. Class & Object
# Create a class `Student` with:
# * attributes: name, age, marks
# * method: `display()` to print student details

# 👉 Create 2 objects and call the method.

class Student:
  def __init__(self,name,age,marks):
    self.name=name
    self.age=age
    self.marks=marks
    
  def display(self):
    print("Name:",self.name)
    print("Age:",self.age)
    print("Marks:",self.marks)
    
    
s1=Student("Sarah",20,78)
s1.display()
s2=Student("Amirah",12,99)
s2.display()




# ### 2. Constructor Practice

# Create a class `Car`:
# * attributes: brand, model, year
# * initialize using constructor
# * method `show_info()`

class Car:
  def __init__(self,brand, model, year):
    self.brand=brand
    self.model=model
    self.year=year
    
  def show_info(self):
    print("Brand:",self.brand)
    print("Model:",self.model)
    print("Year:",self.year)

c1=Car("Audi","A10",2026)
c1.show_info()




# ### 3. Instance vs Class Variable

# Create a class `Employee`:

# * class variable: `company_name = "ABC Ltd"`
# * instance variables: name, salary

# 👉 Print both for multiple objects.

# ---

class Employee:
  company_name = "ABC Ltd"
  def __init__(self,name, salary):
    self.name=name
    self.salary=salary
    
e1=Employee("Sarah",12000)
e2=Employee("Aira",62000)
print(Employee.company_name)
print(e1.name)
print(e1.salary)
print(e2.name)
print(e2.salary)




# # 🔹 Intermediate OOP Questions

# ### 4. Method Types

# Create a class `Calculator`:

# * instance method: add numbers
# * class method: change a class variable
# * static method: multiply two numbers

class Calculator:
  my_value=10
  def __init__(self,n1,n2):
    self.n1=n1
    self.n2=n2
    
  def add(self):
    print(self.n1+self.n2)
    
  @staticmethod
  def mul(n1,n2):
    return n1*n2
  
  @classmethod
  def change_val(cls,new_value):
    cls.my_value=new_value

c1=Calculator(12,3)
c1.add()
print(Calculator.mul(2,8))
c1.change_val(20)
print(c1.my_value)



# ### 5. Encapsulation

# Create a class `BankAccount`:

# * private attribute: `__balance`
# * methods:

#   * deposit()
#   * withdraw()
#   * get_balance()

# 👉 Try accessing balance directly (should not work).

# ---

class BankAccount:
  def __init__(self,acc,bal):
    self.account=acc
    self.__balance=bal
  
  def deposit(self,amount):
    print("Rs",amount,"was deposited")
    self.__balance+=amount
    print("Current balance:",self.__balance)
  
  def withdraw(self,with_amount):
    print("Rs",with_amount,"was withdrawn")
    self.__balance-=with_amount
    print("Current balance:",self.__balance)
    
  def get_balance(self):
    return self.__balance
    
    
b1=BankAccount("HBL",5000)
print(b1.account)
b1.deposit(1000)
b1.withdraw(500)
print(b1.get_balance())






# ### 6. Inheritance (Important 🔥)

# Create:

# * Parent class `Animal` → method `speak()`
# * Child class `Dog` → override method

# 👉 Show method overriding.

# ---

class Animal:
  def speak(self):
    print("animal speak")

class Dog(Animal):
  def speak(self):
    print("dog speak")
    
d1=Dog()
d1.speak()
  


# ### 7. Multilevel Inheritance

# Create:

# * `Person` → name
# * `Student` → adds marks
# * `GraduateStudent` → adds degree

# 👉 Display all info.

# ---

class Person:
  def __init__(self,name):
    self.name=name
    
class Student(Person):
  def __init__(self,name,marks):
    super().__init__(name)
    self.marks=marks
    
class GraduateStudent(Student):
  def __init__(self,name,marks,degree):
    super().__init__(name,marks)
    self.degree=degree
    
g1=GraduateStudent("Sarah",89,"A")
print(g1.name)
print(g1.marks)
print(g1.degree)
  




# ### 8. Multiple Inheritance

# Create:

# * `Father` → method `skills()`
# * `Mother` → method `skills()`
# * `Child` inherits both

# 👉 Call both methods.

# ---

class Father:
  def skills(self):
    print("Father is caring")
    
class Mother:
  def skills(self):
    print("Mother is loving")
    
class Child(Father,Mother):
  print("I am child")
  
c1=Child()
c1.skills()




# # 🔹 Advanced Thinking Questions

# ### 9. Polymorphism

# Create a class `Shape`:
# * method `area()`

# Create:
# * `Rectangle`
# * `Circle`
# 👉 Same method name but different implementations.

class Shape:  
  def area(self):
    pass
    
class Rectangle(Shape):
  def __init__(self,len,width):
    self.len=len
    self.width=width
    
  def area(self):
    print("Rectangle:",self.len*self.width)
    
class Circle(Shape):
  def __init__(self,radius):
    self.radius=radius
  
  def area(self):
    print("Circle:",(22/7)*self.radius*self.radius)
    
Shape=[Rectangle(2,3),Circle(3)]
for s in Shape:
  s.area()

  
  


# ### 10. Real-Life Project Type Question ⭐

# Create a class `Library`:

# * add_book()
# * remove_book()
# * show_books()

# 👉 Use list to store books.

# ---


class Library:
  def __init__(self):
    self.books=[]
  def add_book(self,book):
    self.books.append(book)
    
  def remove_books(self,book):
    self.books.remove(book)
    
  def show_books(self):
    print(self.books)

l1=Library()
l1.add_book("Namal")
l1.add_book("Abe Hayat")
l1.add_book("Peer e kamil")
l1.add_book("Mushaf")
l1.show_books()
l1.remove_books("Abe Hayat")
l1.show_books()


# ### 11. Magic Method

# Create a class `Number`:
# * override `__add__()`
#   👉 Add two objects using `+`

# ---

class Number:
  def __init__(self,num):
    self.num=num
    
  def __add__(self,other):
    return self.num+other.num
  
n1=Number(2)
n2=Number(3)
print(n1+n2)
    





# ### 12. Challenge Question 🔥

# Create a class `StudentManagementSystem`:

# * add student
# * search student
# * display all students

# 👉 Use list/dictionary + OOP

class StudentManagementSystem:
  def __init__(self):
    self.students={}
  def add(self,name,marks):
    self.students[name]=marks
  
  def search(self,name):
    print(self.students.get(name))
    
  def show(self):
    print(self.students)

sm=StudentManagementSystem()
sm.add("Sarah",89)
sm.add("Ali",66)
sm.show()
sm.search("Ali")
