# sets --- collection of unordered items
# unique and immutable  (hashable)

# int, float, boolean, string and tuple ---- can store in sets bcz they are not changeable
# list and dict -- cannot store in sets bcz they are changeable



# sets ignore duplicate values
# don't follow any order
num = {1,2,3,4,5,"sarah",4,5,23,"sarah"}
print(num)
print(type(num))
print(len(num))  # ignore duplicate value

num = {}  # empty dict
print(type(num))


num = set()  # empty set
print(type(num))