def check_for_word():

  word="learning"
  with open("C:/Users/Home/Desktop/Python/Lecture 7/Practice/practice.txt","r") as f:
    data=f.read()
    if(data.find(word) != -1):
      print("found")
    else:
      print("not found")

check_for_word()