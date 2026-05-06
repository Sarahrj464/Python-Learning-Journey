# w+ --- open for read and write
# w+ truncate (overwrite) the file

f=open("C:/Users/Home/Desktop/Python/Lecture 7/w+/plus.txt","w+")
print(f.read())
f.write("abc")
f.close()