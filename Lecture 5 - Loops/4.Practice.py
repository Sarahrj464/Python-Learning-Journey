# sum of first n num (1-5)
# 1+2+3+4+5=15

i=1
sum=0
while i<=5:
  sum=sum+i
  i+=1
print("Sum is",sum)


# for loop
sum=0
for i in range(1,6):
  sum+=i
print("Total sum:",sum)



# find fact of first n num
fact=1  #if we take 0 then ans remain 0
num=1
while num<=5:
  fact=fact*num
  num+=1
print("factorial is:",fact)
  

# fact 1 to 6
f=1
for x in range(1,7):
  f=f*x
print(f)