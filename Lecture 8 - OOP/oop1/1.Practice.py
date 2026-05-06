class Student:
  
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
    
  def get_average(self):
    sum=0
    for val in self.marks:
      sum+=val
    print("Hello",self.name,"your marks is:",sum/3.0)
    
    
s1=Student("Sarah",[92,96,98])
# print(s1.name)
# print(s1.bio)
# print(s1.chem)
# print(s1.phy)

s1.get_average()

s1.name="Amirah"
s1.get_average()