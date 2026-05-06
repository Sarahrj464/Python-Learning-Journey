# class -- blueprint for creating objects
class Student:
  name="Sarah"
  
  # constructor (__init__)  -- automatically invoke at object creation
  # self is always first parameter
  # constructor take multiple parameters
  def __init__(self,fullname):
    self.name=fullname
    # print(self)
    print("add new student in database")
   
# object -- instances of class
s1=Student("Sarah")
# print(s1)
print(s1.name)

s2=Student("Amirah")
print(s2.name)



# example
class Car:
  color="green"
  brand="civic"
  
  # class attribute
  car_name="Cars Showroom"
  color="blue"
  
  # default constructor
  def __init__(self):
    pass
  
  # parametrized constructor
  def __init__(self,color,brand):
    self.color=color
    self.brand=brand
    print("Add new data in database...")
    
  # methods
  def welcome(self):
    print("Welcome",self.color)
    
    
  def get_brand(self):
    return self.brand
    
c1=Car("green","civic")
print(c1.color,c1.brand)

# method
c1.welcome()
print(c1.get_brand())

# attribute
# print(Car.car_name)
# print(c1.car_name)