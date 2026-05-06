# tuples --- built-in data type that create immutable seq of values
# used parenthesis
tup=(3,7,5,6,2)
print(tup)
print(type(tup))
print(tup[3])
# tup[0]=44  -- immutable like string
# print(tup)


# valid tuple
tup = ()  # empty
print(tup)
print(type(tup))


# single value tuple always create by write comma after number
tup = (1,)
print(type(tup))


# if we write single value in tuple then python consider it an integer
tup = (1)
print(type(tup)) # int

tup = (2.0)
print(type(tup))  # float


# slicing in tuple
tup = (1,3,5,6)
print(tup[1:3])
print(tup[-4:-1])


