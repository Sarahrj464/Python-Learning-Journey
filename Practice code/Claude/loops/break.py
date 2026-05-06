# Loop Control (break/continue)

# Print numbers 1 to 20 but skip multiples of 3 --- 3,6,9,12,15,18
for i in range(1,21):
  if(i%3==0):
    continue
  print(i)



# Ask user to enter numbers in a loop — stop when they enter a negative number, print sum of all entered numbers
sum=0
while True:
  num=int(input("Enter a number: "))
  if(num<0):
    break
  sum=sum+num
print("Total sum is:",sum)

  


# Print this pattern:

# * 
# * * 
# * * * 
# * * * * 
# * * * * *
for i in range(1,6):
  for j in range(i):
    print("*",end=" ")
  print()  # go to newline
    
  