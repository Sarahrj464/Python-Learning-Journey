# static method -- don't use self parameter / work at class level

class Student:
  
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
    
  # static method -- class level
  # use decorator
  
  # decorator -- allow us to wrap another function in order to extend wrapped function behavior without permanenlty modify it
  
  # normal function ke behavior ku change krke use static bna dya
  
  # function which is decorator -- it takes function as parameter and give function as output
  @staticmethod
  def hello():
    print("hello")
    
  def get_average(self):
    sum=0
    for val in self.marks:
      sum+=val
    print("Hello",self.name,"your marks is:",sum/3.0)
    
    
s1=Student("Sarah",[92,96,98])
s1.get_average()

s1.name="Amirah"
s1.get_average()
s1.hello()