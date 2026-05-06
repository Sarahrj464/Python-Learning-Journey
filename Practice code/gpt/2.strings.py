# # Level 2 — Strings

# # Q5.
# # Take a name as input and print it in uppercase.
# name=input("Enter name: ")
# print(name.upper())




# # Q6.
# # Write a program that counts the number of vowels in a string.
# str = "python"
# vowels = "aeiou"
# count=0
# for el in str:
#   if el in vowels:
#     count=count+1
# print(count,"vowel in",str)


# # Example
# # Input: "python"
# # Output: 1




# # Q7.
# # Check whether a given string is a palindrome.

# # Example
# string = "madam"
# new_string=string[::-1]

# if(string==new_string):
#   print("Palindrome")
# else:
#   print("not Palindrome")


# Input: madam
# Output: Palindrome




# Part 2: Strings

# 6️⃣ Take a string from the user and print:

# its length
# first character
# last character

string=input("Enter string: ")
print(string)
print("length:",len(string))
print(string[0])
print(string[len(string)-1])




# 7️⃣ Count how many times the letter "a" appears in a string.

count=0
myString=input("Enter a string: ")
for i in myString:
  if ('a' in i):
    count+=1
print(count)










# 8️⃣ Reverse a string without using built-in reverse functions.

myStr="Sarah"
print(myStr[::-1])



# 9️⃣ Check whether a string is a palindrome.

# Example:
# madam → palindrome
# hello → not palindrome

word="madam"
rev_word=word[::-1]

if (word==rev_word):
  print("palindrome")
else:
  print("not palindrome")




# 🔟 Take a string and print it in uppercase and lowercase.
mystring="Amirah"
print(mystring.upper())
print(mystring.lower())