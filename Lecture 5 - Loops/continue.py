# continue --- only terminate current loop iteration

i=1
while i<=5:
  if(i==3):
    i+=1
    continue   # skip (means statement after continue not work if i=3)
  print(i)
  i+=1
  
  
  
# print odd
x=1  
while x<=10:
  if(x%2!=0):  # 2 4 6 8 10
    x+=1
    continue
  print(x)
  x+=1
  
  
    