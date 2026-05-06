# Abstraction -- thing that is hide / unclear / only show important features / remove unnecessary details

# Hiding implementation details of class and only show useful features to user

# Encapsulation
# Inheritence
# Polymorphism 

class Car:
  def __init__(self):
    self.acc=False
    self.brk=False
    self.clutch=False
    
  def start(self):
    # unnecessary details
    self.clutch=True
    self.acc=True
    print("car started..")
    
car1=Car()
car1.start()