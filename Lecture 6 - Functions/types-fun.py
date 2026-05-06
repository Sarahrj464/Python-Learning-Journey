# functions in python
# 1. built-in --- already define in language
# 2. user-defined


# built-in 
# ex: print(),range(),len(),type()

print("hello","sarah",end=" ")  #sep = " "
print("welcome")  #end=\n 



# default parameters  -- no arguments passed
def calProd(a=1,b=1):  # both arguments are default (value=1) ; 1st non-default and 2nd default (possible) ; 1st default and 2nd non-default (gives error)
  return a*b

prod=calProd(3)
print(prod)