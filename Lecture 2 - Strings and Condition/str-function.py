# endswith
str="I am Sarah Rajput"
print(str.endswith("put"))
print(str.endswith("rah"))



#capitalize -- only capitalize 1st character
str1="i Am Learning Python"
print(str1.capitalize())  # this change reflect only at once, original string has no change
print(str1)

# make change in original string
str1=str1.capitalize()
print(str1)



# replace -- old with new
print(str1.replace("python","C++"))
print(str1.replace("a","z"))



# find --- find first occurence of char
print(str1.find("a"))
print(str1.find("n"))



# count --- used to count how many times occur in string
print(str1.count("am"))
print(str1.count("n"))