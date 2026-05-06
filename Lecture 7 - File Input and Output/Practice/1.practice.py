# create file using python and write following data

with open("C:/Users/Home/Desktop/Python/Lecture 7/Practice/practice.txt","w") as f:
  f.write("Hi everyone\nwe are learning File I/O\n")
  f.write("using Java\nI like programming in Java")



# to replace any data, first we read file
with open("C:/Users/Home/Desktop/Python/Lecture 7/Practice/practice.txt","r") as f:
  data=f.read()


# data is available in string form so use .replace() method 
new_data=data.replace("Java","python")
print(new_data)
  
  
# again write update data in file
with open("C:/Users/Home/Desktop/Python/Lecture 7/Practice/practice.txt","w") as f:
  f.write(new_data)
  

