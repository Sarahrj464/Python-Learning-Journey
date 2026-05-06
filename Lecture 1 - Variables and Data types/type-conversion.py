# Conversion
# 1. Type conversion (implicit) --- automatic conversion
# 2. Type casting  --- manual conversion which is done forcefully

# implicit type conversion
a=10
b=2.5
c="20"
print(a+b)  #int + float --- float is superior so ans must come in float
# print(a+c)  --- give error bcz string and int -- not type conversion 



# Type casting --- forcefully convert one data type value into another
x=int("10")
y=5.25
print(type(x))
print(x+y)


a1=str(10.2)
print(a1)
print(type(a1))