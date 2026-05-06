# file I/O ---- file open,close,del,read,write
# used to perform operations on file

# RAM --- variables create in RAM (volatile) -- temporary data

# to store data permanently -- we store data in files / files store in ssd of computer


# types
# 1. text files -- data store in character form (.txt, .docx .log)
# 2. binary files --- .mp4  .mov  .png
# (all data of both files stored in form of 0 1 in computer)


# open file -- read entire file
f = open("C:/Users/Home/Desktop/Python/Lecture 7/read/demo.txt", "r")  # by default text mode -- we can combine 2 modes at time 

# specify num of characters
data=f.read(5)
# data=f.read()
print(data)
print(type(data))
f.close()





# open file -- read one line
f = open("C:/Users/Home/Desktop/Python/Lecture 7/read/demo.txt", "r")

# if we read entire file at once then readline does not read line again
# data=f.read()
# print(data)


# read one line from file
line1=f.readline()  # create 1 line space in output bcz each line ends with /n in text file 
print(line1)

line2=f.readline()
print(line2)

line3=f.readline()
print(line3)

# empty line create
line4=f.readline()
print(line4)
f.close()



# read -- read entire file

# readline -- agr aik dfa complete file read kr le and then readline kia tu wo empty line space create kre ga bcz file is already read / same agr readline kr rhy and lines end hugyen tb bhi agr readline kren gy tu empty line space ae gy