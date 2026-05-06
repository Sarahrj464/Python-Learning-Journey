# # Q1. Write a function that takes a list and returns only the odd numbers.

def oddNum(list):
  odd = []
  for n in list:
    if(n%2!=0):
      odd.append(n)
  return odd

mylist = [1,2,3,4,5]
result=oddNum(mylist)
print(result)


# # Q2. Take a string from user and write a function to check if it is a palindrome or not.

def checkPalin(string):
  new_string=string[::-1]
  if(new_string==string):
    print("palindrome")
  else:
    print("not palindrome")
    
string = input("Enter a string: ")
checkPalin(string)



# # # Q3.
# # # pythonstudents = {"Ali": 45, "Sara": 80, "Ahmed": 55, "Zara": 30}
# # # Print only the failed students (marks < 50).

pythonstudents = {
  "Ali": 45, 
  "Sarah": 80, 
  "Ahmed": 55, 
  "Zara": 30
}
for n in pythonstudents:
  if pythonstudents[n]<50:   #pythonstudents["Ali"]=45   45<50
    print(n)
for val in pythonstudents.values():
  if val<50:    # 45<50
    print(val)
for k,v in pythonstudents.items():   # key:value
  if v<50:    # val<50
    print(k,v)   # print both



# # # Q4. Write a recursive function that returns the sum from n down to 1.

def sum(n):
  if n==0:
    return 0
  return sum(n-1)+n

num=int(input("Enter number: "))
result=sum(num)
print("Sum is",result)


# print 1st 5 num
def show(n):
  if(n==0):
    return 0
  show(n-1)
  print(n)

show(5)



# # Q5. Take 5 numbers from user, store in a list, then print the largest number and its index.

list = []
for i in range(1,6):
  n=int(input(f"Enter number {i}: "))
  list.append(n)
largest=list[0]
largest_idx=0

for i in range(len(list)):
  if(list[i]>largest):
    largest=list[i]
    largest_idx=i
    
print("Number:",largest)
print("Index:",largest_idx)


