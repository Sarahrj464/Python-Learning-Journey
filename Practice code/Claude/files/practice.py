# Basic Read
# Create a file info.txt with your name, age, city on separate lines. Read and print each line separately.

with open("info.txt","w") as f:
  f.write("Sarah\n22\nLahore")
  
with open("info.txt","r") as f:
  data=f.read()
  print(data)
  
  
  
# Write
# Take 3 sentences from user and write them to a file notes.txt. Then read and print the file.

a=input("Enter sentence 1: ")
b=input("Enter sentence 2: ")
c=input("Enter sentence 3: ")

with open("notes.txt","w") as f:
  f.write(a)
  f.write("\n")
  f.write(b)
  f.write("\n")
  f.write(c)
  
with open("notes.txt","r") as f:
  data=f.read()
  print(data)
  
  
  
# # Count
# # You have a file words.txt with this content:
# # "apple,banana,mango,grape,kiwi"
# # Count how many words are in the file.

# count=0
with open("words.txt","r") as f:
  data=f.read()
  fruits=data.split(",")
  print(len(fruits))
  # for val in fruits:
  #   count+=1
  # print(count)
  
  
  
# # Search
# # You have a file students.txt with names on separate lines. Take a name from user and check if that name exists in the file — print "Found" or "Not Found".

with open("students.txt","r") as f:
  data=f.read()
  name=input("Enter a name: ")
  
  if(name in data):
    print("found")
  else:
    print("not found")



# # Append
# # Create a file log.txt. Ask user to enter 3 messages one by one — append each message to the file on a new line. Then print the full file.

m1=input("Enter a message: ")
m2=input("Enter a message: ")
m3=input("Enter a message: ")

with open("log.txt","a") as f:
  f.write(m1)
  f.write("\n")
  f.write(m2)
  f.write("\n")
  f.write(m3)
  
with open("log.txt","r") as f:
  data=f.read()
  print(data)