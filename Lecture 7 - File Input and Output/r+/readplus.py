# r+ -- overwrite data at starting of file
# r+ -- open for reading and writing 

f=open("C:/Users/Home/Desktop/Python/Lecture 7/r+/read.txt","r+")
f.write("abc")

# read whan se start huga jahan pr pointer khra hy
# in current case, abc overwrite Thi so pointer ab s pr khra hy and s se ownward read kre ga
print(f.read())
f.close()