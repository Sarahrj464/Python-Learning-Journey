# Property
# use @property decorator 
# jb attribute ke value function pr depend kr rhy hu then us function ku @property bna dety

class Student:
  def __init__(self,phy,chem,math):
    self.phy=phy
    self.chem=chem
    self.math=math
    # self.percentage=str((self.phy+self.chem+self.math)/3) + "%"
    
  # def calPercentage(self):
  #   self.percentage=str((self.phy+self.chem+self.math)/3) + "%"
  
  @property
  def percentage(self):
    return str((self.phy+self.chem+self.math)/3) + "%"
    
s1=Student(89,78,90)
print(s1.percentage)

# change marks
s1.phy=85
# print(s1.phy)
print(s1.percentage)

# method 1
# s1.calPercentage()
# print(s1.percentage) #original value ke according hi ae gy means ju previous thy same ae gy