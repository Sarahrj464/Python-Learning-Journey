# # Level 4 — Dictionary & Set

# # Q11.
# # Create a dictionary to store student name and marks and print all keys and values.

# # Example
# # {"Ali":80, "Sara":90, "Ahmed":75}

# dict = {
#   "Ali":80, 
#   "Sarah":90, 
#   "Ahmed":75
# }
# print(dict)


# # Q12.
# # Write a program that finds common elements between two lists using sets.

# # Example

# # list1 = [1,2,3,4]
# # list2 = [3,4,5,6]
# # Output: {3,4}

# list1 = [1,2,3,4]
# list2 = [3,4,5,6]
# new_list1=set(list1)
# new_list2=set(list2)
# print(new_list1.intersection(new_list2))


# Part 4: Dictionary & Set

# 16️⃣ Create a dictionary to store student name and marks and print the marks of a specific student.

# Example
# {"Ali":80,"Sara":90}


dict = {
  "Ali":80,
  "Sarah":90
}
print(dict["Sarah"])





# 17️⃣ Count frequency of each character in a string using dictionary.

# Example
# hello → {h:1, e:1, l:2, o:1}

string = "hello"
freq={}
for char in string:
  if char in freq:
    freq[char]+=1
  else:
    freq[char]=1
print(freq)


# 18️⃣ Create a set from a list and remove duplicates.

list = [1,2,2,3,4,4,5]
print(set(list))





# 19️⃣ Find intersection of two sets.

s1={1,2,3,4}
s2={2,3,7,5}
print(s1.intersection(s2))



# 20️⃣ Write a program to print all keys and values of a dictionary.

student = {
  "name":"Sarah",
  "age":22,
  "city":"Lahore"
}
print(student)