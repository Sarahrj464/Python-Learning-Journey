# del --- delete object properties or obj itself
# del s1 -- delete entire object
# del s1.name -- delete single attribute

class Student:
  def __init__(self,name):
    self.name=name
    
s1=Student("Sarah")
print(s1.name)
del s1
print(s1)