# Part 7: File Handling

# 31️⃣ Create a file and write 5 lines of text into it.


with open("C:/Users/Home/Desktop/Python/gpt/file.txt","w") as f:
  f.write("Hello, Sarah\nWelcome to Python\n")
  f.write("Are u ready?\nSo let's start\nBest of Luck")


# 32️⃣ Read the entire file and print its content.
with open("C:/Users/Home/Desktop/Python/gpt/file.txt","r") as f:
  data=f.read()
  print(data)


# 33️⃣ Count how many words exist in a file.
with open("C:/Users/Home/Desktop/Python/gpt/file.txt","r") as f:
  data=f.read()
  words=data.split()
  print(words)
  print(len(words))




# 34️⃣ Count how many lines exist in a file.

def show():
  line_no=0
  data=True
  with open("C:/Users/Home/Desktop/Python/gpt/file.txt","r") as f:
    while True:
      data=f.readline()
      if not data:
        break
      line_no+=1
    print(line_no)
show()
    
  

# 35️⃣ Write a program to append text to an existing file.
with open("C:/Users/Home/Desktop/Python/gpt/file.txt","a") as f:
  f.write("Keep practice\nKeep Growing")