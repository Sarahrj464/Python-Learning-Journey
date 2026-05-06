with open("C:/Users/Home/Desktop/Python/Lecture 7/with/test.txt","r") as f:
  data=f.read()
  print(data)
  
# f.close() -- with automatically close the file so no need to close it




with open("C:/Users/Home/Desktop/Python/Lecture 7/with/test.txt","w") as f:
  f.write("new data")
