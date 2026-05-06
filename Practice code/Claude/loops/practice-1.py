# Q1 — String + Condition
# Take a word from user — print how many vowels and how many consonants are in it.

vowels="aeiou"
v=0
c=0
word = input("Enter any word: ")
for i in word:
  if i in vowels:
    print(i,"vowels")
    v+=1
  else:
    print(i,"consonant")
    c+=1
    
print(v,"vowels")
print(c,"consonant")
    


# Q2 — List + Loop
# You have [5, 12, 33, 7, 45, 2, 18]
# Print even numbers and their sum separately.

list = [5, 12, 33, 7, 45, 2, 18]
s=0
for i in list:
  if(i%2==0):
    print(i)
    s=s+i
print("Sum of even num:",s)



# # Q3 — Dictionary + Condition
# # pythonproducts = {"apple": 50, "banana": 20, "mango": 80, "grape": 15}
# # Print only products that cost more than 30.


products = {"apple": 50, "banana": 20, "mango": 80, "grape": 15}
for i in products:
  if (products[i]>30):
    print(i)


# Q4 — Loop + Counter
# Take a sentence from user — count how many words are in it.

# Example: "I love Python" → 3 words


sentence = input("Enter a sentence: ")
print(len(sentence.split()))






# Q5 — Mixed
# Take 5 numbers from user using a loop, store in a list, then print:

# Sum
# How many are even
# How many are odd

numbers = []
s=0
even=0
odd=0
for i in range(1,6):
  n=int(input(f"Enter number {i}: "))
  numbers.append(n)
  s=s+n
  if(n%2==0):
    even+=1
  else:
    odd+=1
print("Sum is:",s)
print("Even numbers are:",even)
print("Odd numbers are:",odd)
  
