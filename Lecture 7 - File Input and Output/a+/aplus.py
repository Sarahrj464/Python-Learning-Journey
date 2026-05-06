# a+ -- open for read and write
# data is positioned at end of file

f=open("C:/Users/Home/Desktop/Python/Lecture 7/a+/demo1.txt","a+")

# kuch bhi read ni huga bcz pointer end pr hy
print(f.read())

# append at the end 
f.write("abc")
f.close()