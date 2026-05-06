# function -- block of statements that perforn specific task
# why we use functions --- to avoid repetition (redundancy of code)
# redundant code shows bad developer performance

def calSum(a,b):  # parameters (input)
  sum=a+b
  print(sum)
  return sum  # output

calSum(12,34)




# function definition
def cal(x,y):  #parameters
  return x+y

sum = cal(2,3)   #funcional call(arguments)
print(sum)





def printHello():
  print("hello")

printHello()
printHello()
printHello()
printHello()
printHello()



# Two things optional in functions
# 1. no pass parameters
# 2. never return any value


def call():
  print("Sarah")

output=call()
print(output)  #None (no return any value)




# average of 3 num
def findAverage(a,b,c):
  return (a+b+c)/3.0
  # sum = a+b+c
  # avg=sum/3
  # print(avg)

# findAverage(2,3,4)
avg=findAverage(2,5,8)
print(avg)