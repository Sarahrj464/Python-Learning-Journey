# # print 1-100
# i=1
# while i<=100:
#   print(i)
#   i=i+1
# print("ended")


# # print 100-1
# j=100
# while j>=1:
#   print(j)
#   j-=1
# print("ended")



# # multiplication of num
# n=5
# i=1
# while i<=10:
#   print(f"{n} X {i} = {n*i}")
#   i+=1
# print("finish")


# # print given num
# num = [1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(num):
#   print(num[idx])
#   idx+=1
  
  
  
# # print names  -- traversing
# heroes = ["ironman","superman","batsman","ironmaster","techman"]
# index=0
# while index<len(heroes):
#   print(heroes[index])
#   index+=1
  
  
n = (1,4,64,9,16,25,36,49,64,81,100)
x=64
i=0
while i<len(n):
  if(n[i]==x):
    print("Found at index",i)
    break # loop terminate
  else:
    print("finding..")
  i+=1
 
