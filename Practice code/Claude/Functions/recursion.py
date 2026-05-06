# Recursion
# Q6 — Classic
# Write a recursive function factorial(n) that returns factorial of n.

def factorial(n):
  if n==0 or n==1:
    return 1
  return factorial(n-1)*n
f=factorial(5)
print("Factorial is:",f)

# factorial(5) → 120




# Q7 — Sum
# Write a recursive function total(n) that returns sum of 1 to n.
def total(n):
  if n==0:
    return 0
  return total(n-1)+n
sum=total(4)
print("Sum:",sum)

# total(4) → 10






# Q8 — String
# Write a recursive function reverse(s) that reverses a string.

# reverse("hello") → "olleh"

def rev(s):
  if len(s)==0:
    return s
  return rev(s[1:])+s[0]

name=rev("Sarah")
print(name)