# Write a function that takes a string and returns how many words start with a vowel.
string = "apple is an orange"
new_string=string.split()

vowels="aeiou"
count=0
for i in new_string:
  if i[0] in vowels:
    count+=1
print(count)





# using function
def count(string):
  vowels="aeiou"
  c=0
  for i in string:
    if i[0] in vowels:
      c=c+1
  return c
    
mystring = "hey i am sarah"
newstring=mystring.split()
result=count(newstring)
print("Count words:",result)