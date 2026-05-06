# .keys() --- return all keys
# .values() -- return all values
# .items() -- return all (key,val) as tuple
# .get("key") -- return key according to value
# .update(newDict) -- insert new item in dict or update any old key value

#  sorted() --- works in list,set,dict
#  sort() -- only works in list

# dict.keys()

student = {
  "name":"Sarah",
  "subjects":{
    "phy":78,
    "chem":88,
    "math":99
  }
}
# nested keys never return
print(student.keys())


# convert dict into list or tuple -- typecasting
print(list(student.keys()))

print(len(student))

print(len(list(student.keys())))



# dict.values()
# we can store dictionary values into list and vice versa
print(student.values())
print(list(student.values()))



# .items()  --- return tuple
# print(student.items())
# print(list(student.items()))

pairs = student.items()
print(pairs)

# we can access individual items of list not dict
pairs = list(student.items())
print(pairs)
print(pairs[0])
print(pairs[1])



# .get(key) --- return value of key
# differ between .get() and dict["key"] -- directly access any key value or by using get method

# print(student["name1"])  # gives error -- iske bad agr koe bhi code lekhen gy wo execute ni huga
print(student.get("name1"))  # gives none
print("Hello")
print("Sarah")
print("Welcome")
print("Python course")




# .update(newDict) -- add in old dict
student.update({"city":"Lahore"})
print(student)

new_dict = {"city":"Lahore","age":22,"name":"Ali"}
student.update(new_dict)
print(student)