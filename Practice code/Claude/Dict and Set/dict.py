# Create a dictionary with your name, age, and city. Print each value separately.
info = {
  "name":"Sarah",
  "age":22,
  "city":"Lahore"
}
print(info)


# Add a new key "email" to the dictionary and print the updated dictionary.
info.update({"email":"sarah20@gmail.com"})
print(info)



# Take a student's marks in 3 subjects as a dictionary. Print the subject with the highest marks.
marks = {
  "math":70,
  "phy":90,
  "chem":96,
}
max_Marks=max(marks,key=marks.get)
print(max_Marks,marks[max_Marks])

min_Marks=min(marks,key=marks.get)
print(min_Marks,marks[min_Marks])






# Count how many times each word appears in a sentence using a dictionary.

# Example: "apple banana apple orange banana apple" → {"apple": 3, "banana": 2, "orange": 1}


# fruits = {
#   "apple", "banana", "apple", "orange", "banana", "apple"
# }
# print(fruits)
# newlist = list(fruits)[0]
# print(newlist)
# print(len(newlist))
