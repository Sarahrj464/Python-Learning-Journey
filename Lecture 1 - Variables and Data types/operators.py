# operators --- performs operation between operands

# Arithematic operator
a=5
b=2
sum=a+b
print(sum)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) # gives remainder
print(a^b)  # gives power


# Relational/ Comparison Operators ---- gives true/false in output
x=10
y=5
print(a==b)  # False
print(a!=b) # True
print(a>=b)  # True
print(a<=b)  # False
print(a<b)  # False
print(a>b)  # True


# Assignment operators
a1=20
a2=15
a3=5
a4=2
a5=20
# a1=a1+10
a1+=10
a2-=10
a3*=10
a4/=10
a5**=10
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)


# Logical operators
print(not False)
print(not True)

x1=10
x2=5
print(not x1>x2)  #F
print(not x1<x2)  #T


v1=True
v2=False
print("AND operator: ", v1 and v2)  #F
print("OR operator: ", v1 or v2)  #T

print("AND operator: ", (x1>x2) and (x1==x2))  #F
print("OR operator: ", (x1>x2) or (x1==x2))  #T