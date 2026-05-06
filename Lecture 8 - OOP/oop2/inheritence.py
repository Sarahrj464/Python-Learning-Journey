# inheritence -- things inherit from parent to child
# when one class (child/derived) drives prop. and methods from another class (parent/base)

# child/derived --- ju prop. lety hy
# parent/base -- js se prop. le jaty hn

class Car:
  color="black"
  @staticmethod
  def start():
    print("car started")
    
  @staticmethod
  def stop():
    print("car stopped")
    
class ToyotaCar(Car):
  def __init__(self,name):
    self.name=name
    
# multi-level inheritence
class Fortuner(ToyotaCar):
  def __init__(self,type):
    self.type=type
    
    
c1=ToyotaCar("Fortuner")
c2=ToyotaCar("Prado")
# print(c1.name)
print(c1.start())  #inheritence
print(c1.color) 
 
car1=Fortuner("diesel")
car1.stop()





# Types of inheritence
# 1. single  --   base (p) -> derived (c)
# 2. multi-level -- base (p) -> derived (c),(p) -> derived (c)
# 3. multiple -- derived class inherit multiple parent class properties  --- base1 + base2 -> derived

class A:
  varA="Welcome to class A"
  
class B:
  varB="Welcome to class B"
  
class C(A,B):
  varC="Welcome to class C"
  
c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)