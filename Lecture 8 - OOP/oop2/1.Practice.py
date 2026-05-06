class Circle:
  def __init__(self,radius):
    self.radius=radius
    
  def area(self):
    return (22/7)*self.radius*self.radius
  
  def perimeter(self):
    return 2*(22/7)*self.radius
  
c1=Circle(3)
print(c1.area())
print(c1.perimeter())



# employee class
class Employee:
  def __init__(self,role,dept,sal):
    self.role=role
    self.dept=dept
    self.sal=sal
    
  def show(self):
    print("Your Role is:",self.role,"\nYour dept is:",self.dept,"\nYour salary is:",self.sal)
    
class Engineer(Employee):
  def __init__(self,name,age):
    self.name=name
    self.age=age
    super().__init__("HR","CS","3,50,000")
    
e2=Engineer("Sarah",22)
e2.show()


# order
class Order:
  def __init__(self,item,price):
    self.item=item
    self.price=price
    
  # dunder function
  def __gt__(self,order2):
    return self.price>order2.price
  
o1=Order("chips",100)
o2=Order("tea",50)
print(o1>o2)