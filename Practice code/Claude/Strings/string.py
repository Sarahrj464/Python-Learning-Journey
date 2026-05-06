# Take your full name and print it in all capital letters

name=input("Enter full name: ")
print(name.upper())



# Count how many characters are in a sentence
tense="Hey I am Sarah, a Developer"
print(len(tense))


# Reverse any word  --- [start:stop:steps]
print(tense[::-1])  # complete sentence reverse
tense1=tense[9:14]  # reverse a word
print(tense1[::-1])



# String Concatenation
string1="Sarah"
string2="Rajput"
print(string1 + " " + string2)


# String Repetition
print(string1 * 3)


# Check if a word is Palindrome
word="Sarah"
reverse=word[::-1]
if(reverse==word):
  print("palindrome")
else:
  print("not palindrome")
  
  
#  Replace a word in sentence
sentence="I am Sarah"
print(sentence.replace("Sarah","Amirah"))


# Split a sentence into words
print(sentence.split())