# For Loop

# Print each character of your name separately
# name="Sarah"
# for char in name:
#   print(char)
  
  
  
# From a list of numbers, print only those greater than 10
n=[2,5,8,10,15,20]
# for i in range(len(n)):
#   if(n[i]>10):
#     print("Numbers greater than 10 are:",n[i])

for i in n:
  if(i>10):
    print(i)


# Calculate sum of all numbers in a list [1, 2, 3, 4, 5]
nums=[1,2,3,4,5]
sum=0
for i in nums:
  sum+=i
print(sum)
  