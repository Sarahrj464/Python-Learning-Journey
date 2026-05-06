# recursion --- when function call itself repeatedly  (just like loops )

# loops and recursion are inter-related
# ju kam loop se hu skty wo recursion se bhi kr skty and vice versa

# loops --- for beginner level problems
# recursion --- for dsa


def show(n):
  # BASE CASE --- without base case, recursion run infinite time that crash program
  
  if(n==0): # agr base case define na kia tu recursion 1 0 -1 -2 ... chlty jae gy
    return # return control, not value
  print(n)
  show(n-1)  #recursive call
  print("end")
  
show(5)   # 5=n  4=n-1  3=n-2  2=n-3  1=n-4



# factorial using recursion
def fact(n):
  if(n==0 or n==1):
    return 1
  return fact(n-1)*n
f=fact(4)
print(f)



# Practice
# first n natural num --- simple function
def num(n):
  sum=0
  for i in range(1,n+1):
    sum+=i
  print(sum)

num(10)


# first n natural num --- using recursion
def sum(n):
  if(n==0):
    return 0
  return sum(n-1)+n
s=sum(5)
print("sum:",s)


# print all elements in a list
names = ["sarah","ali","amir","asad"]
def show(list,index=0):
  if(index==len(list)):
    return
  print(list[index])
  show(list,index+1)
  
show(names)
