# private --- cannot acces outside the class

# attributes and methods are working like private but not exactly private

class Account:
  def __init__(self,acc_no,acc_pass):
    self.acc_no=acc_no
    
    self.__acc_pass=acc_pass
  # access inside class
  def reset__pass(self):
    print(self.__acc_pass)
    
a1=Account("12345","abcde")
print(a1.acc_no)
# private attr
# print(a1.__acc_pass)  #gives error


# private attr
class Person:
  __name="anonymuous"
  
# private method
  def __hello(self):
    print("Hello Sarah")
    
  def welcome(self):
    self.__hello() 
  
p1=Person()
# print(p1.__name)
print(p1.welcome())


