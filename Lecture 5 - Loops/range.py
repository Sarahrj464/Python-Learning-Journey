# range --- sequence of characters
# start from 0
# range -- start,stop,end 


seq = range(1,5)
print(seq[0])
print(seq[1])
print(seq[2])


# print 1-10
for i in range(1,11):
  print(i)
  

# print 0-9
for x in range(10):   #range(stop)
  print(x)
  
  
for y in range(2,10):  #range(start,stop)
  print(y)
  
  
  
for a in range(2,10,2):  #range(start,stop,step)
  print(a)
  
  
  
for x1 in range(2,51,2):
  print(x1)
  
  
  
  
  
# simple for loop 
value = [10,20,30,40,50]
index=0
for el in value:
  print(el,index)
  index+=1
  
  
  
names = ['a','b','c','d','e']
i=0
char='d'
for ch in names:
  if(ch==char):
    print("char found at:",ch,i)
  i+=1