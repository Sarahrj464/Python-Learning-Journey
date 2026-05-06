# Q1 — Loop + String
# Print each vowel found in the word "education"
word="education"
vowels="aeiou"
for i in word:
  if i in vowels:
    print(i)
  
  
# Q2 — List + Loop
# You have a list [10, 25, 3, 47, 8] — print each number and also print if it's greater than 20 or not.
list = [10,25,3,47,8]
for n in list:
  # print(n)
  if(n>20):
    print(n,"greater than 20")
  else:
    print(n,"not greater than 20")
    
    
    
    
# Q3 — Dictionary + Loop
# You have:

students = {"Ali": 80, "Sara": 45, "Ahmed": 60}

for i in students:
  if(students[i]>=50):
    print(i)



# **Q4 — While Loop**
# Ask user to enter a number repeatedly — stop when they enter 99. Count how many numbers they entered.
count=0
while True:
  n=int(input("Enter number: "))
  if(n==99):
    break
  count+=1
print(count)
  
  
  
# **Q5 — Pattern**
# ```
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


for i in range(1,6):
  for j in range(i):
    print(j+1,end=" ")
  print()