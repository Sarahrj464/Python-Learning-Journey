# with open("C:/Users/Home/Desktop/Python/Lecture 7/Practice/practice4.txt","r") as f:
#   data=f.read()
#   print(data)
#   num=""
#   for i in range(len(data)):
#     if(data[i]==","):
#       print(num)
#       num=""
#     else:
#       num+=data[i]
      
      
      
# 2nd method

count=0
with open("C:/Users/Home/Desktop/Python/Lecture 7/Practice/practice4.txt","r") as f:
  data=f.read()
  num=data.split(",")
  for val in num:
    if(int(val)%2==0):
      count+=1

print(count)