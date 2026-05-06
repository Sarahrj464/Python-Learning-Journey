# super method
# access methods of parent class
# inherit from parent class

class Car:
  def __init__(self,type):
    self.type=type
    
  @staticmethod
  def start():
    print("car started")
    
  @staticmethod
  def stop():
    print("car stopped")
    
class ToyotaCar(Car):
  def __init__(self,name,type):
    # super method 
    super().__init__(type)
    self.name=name
    super().start()

c1=ToyotaCar("fortuner","electric")
print(c1.type)
