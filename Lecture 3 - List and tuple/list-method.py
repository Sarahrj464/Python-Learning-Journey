# list method --- only specific to lists

# append ---  add element at end of list
list = [32,13,24,20]
list.append(50)  #we do mutation in list
print(list)


# sort --- arrange items in order
print(list.sort())  #print none
print(list)

# print in descending order
list.sort(reverse=True)
print(list)

# sorting apply on characters/strings
lists = ["apple","kiwi","cherry","banana"]
lists.sort()
print(lists)

# insert --> add to particular index (index,element)
list.insert(1,55)
print(list)

# remove -- first occurence of element
# pop -- remove element from particular index
list.pop(3)
print(list)