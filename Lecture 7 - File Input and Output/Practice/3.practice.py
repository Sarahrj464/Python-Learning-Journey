def check_for_line():

  word="learning"
  data=True
  line_no=1
  with open("C:/Users/Home/Desktop/Python/Lecture 7/Practice/practice.txt","r") as f:
    while data:
      data=f.readline()
      if(word in data):
       print(line_no)
       return
      line_no+=1
  return -1

check_for_line()
