
# (w) write --- overwrite entire file
# (a) append --- add at the end of file

# write in file
# f=open("C:/Users/Home/Desktop/Python/Lecture 7/demo.txt","w")

# append in file
f=open("C:/Users/Home/Desktop/Python/Lecture 7/write/demo.txt","a")

f.write("\nAfter that I learn flask")

f.close()




# if file does not exist then "a" and "w" can also create a new file

f=open("C:/Users/Home/Desktop/Python/Lecture 7/write/newfile.txt","w")
f.close()



# read and write simultaneously