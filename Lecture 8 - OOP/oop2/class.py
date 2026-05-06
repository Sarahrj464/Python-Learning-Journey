# class method --- hm obj ke through class attribute ku change kren gy
#  -- function ke andar directly class ku access krna

# method 1 --- Person.name=name
# method 2 --- self.__class__.name="Sarah"  
# method 3 --- use @classmethod



# static method --- cannot access or modify class state and generally for utility

class Person:
  # class attribute
  name="anonymuous"
  
  # def changeName(self,name):
  #   self.name=name
    
    # Person.name=name   -- method 1
    
    # self object access class
    # self.__class__.name="Sarah"  --- method 2
    
  @classmethod
  def changeName(cls,name):
    cls.name=name
    
p1=Person()
p1.changeName("Sarah")
print(p1.name)  #sarah
print(Person.name) #anonymuous


# 3 types of functions
# 1. static method -- not access attribute/method of class/instance

# 2. class method (cls)

# 3. instance/normal method (self)