# methods -- functions that belong to obj

class Student:
  # name="Sarah"
  # marks=90
  
  # class attribute
  college_name="ABC college"
  
  def __init__(self,name,marks):
    # object attribute
    self.name=name
    self.marks=marks
    print("add new data...")
    
  # method
  def hello(self):
    print("Hello",self.name)
    
  def get_marks(self):
    return self.marks
    
s1=Student("Sarah",90)
print(s1.name,s1.marks)

s2=Student("Amirah",78)
print(s2.name,s2.marks)

# attribute
print(s1.college_name)

# method
s1.hello()
print(s1.get_marks())
    
