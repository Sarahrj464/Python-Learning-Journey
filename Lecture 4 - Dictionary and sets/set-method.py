# IMP CONCEPTS
# sets --> mutable (new element add or remove) -- unhashable

# sets elements --> immutable (contain hash value that remain same)  -- hashable

# mutable -- hash value change because when we change in original list then hash also change (unhashable)


# Methods
# .add(el)
# .remove(el)

collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("sarah")
collection.add((1,2,3))
# collection.add([1,2,3]) -- lists cannot add in set
# collection.add({"key":"value"}) -- dict cannot add in set
print(collection)
print(len(collection))

collection.clear()
print(collection)

# collection.remove(2)
# print(collection)

# gives error
# collection.remove(20)
# print(collection)


collection = {"hello","sarah","welcome","python","java"}
print(collection.pop())
print(collection.pop())



# union -- combine both set values and add into new set (unique)

set1={1,2,3}
set2={2,3,4,5}
print(set1.union(set2))


# intersection --- contain common values
print(set1.intersection(set2))


# difference --- occur in first set but not in second
set1 = {1,2,3,4,5}
set2 = {3,4,5,6}
print(set1.difference(set2))