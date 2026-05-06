# # Level 5 — Loops

# # Q13.
# # Print numbers from 1 to 10 using a loop.
# for i in range(1,11):
#   print(i)


# # Q14.
# # Print the multiplication table of 5.
# n=5
# for i in range(1,11):
#   print(f"{n} X {i} = {n*i}")





# # Q15.
# # Find the sum of numbers from 1 to n.

# # Example

# # Input: 5
# # Output: 15

# n=int(input("Enter a num: "))
# s=0
# for i in range(1,n+1):
#   s=s+i
# print("Sum:",s)



# 🟢 Part 5: Loops

# 21️⃣ Print numbers from 1 to 20 using for loop.

for i in range(1,21):
  print(i)




# 22️⃣ Print even numbers from 1–50.

for i in range(1,51):
  if (i%2==0):
    print(i)



# 23️⃣ Print multiplication table of a number.

# Example

# 5 × 1 = 5
# 5 × 2 = 10

n=5
for i in range(1,11):
  print(f"{n} X {i} = {n*i}")






# 24️⃣ Calculate factorial of a number using loop.

fact=1
for i in range (1,6):
  fact=fact*i
print(fact)



# 25️⃣ Print this pattern:

# *
# **
# ***
# ****
# *****

for i in range(1,6):
  for j in range(i):
    print("*",end="")
  print()