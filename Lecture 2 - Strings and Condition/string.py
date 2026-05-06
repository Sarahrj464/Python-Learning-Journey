# string -- data type that stores sequence of characters 

str1="Sarah Rajput"
str2='Sarah Rajput'
str3='''Sarah Rajput'''
print(str1)
print(str2)
print(str3)

print("This is my second lecture on Apna College's channel")
print('This is my second lecture on Apna College"s channel')

# escape sequence characters
s="This is my string. \nIt is used to store sequence of characters"
print(s)


s1="This is my string. \tIt is used to store sequence of characters"
print(s1)


# concatenation ---- join 2 strings
a1="Hello"
a2="Sarah"
final=a1+a2
print(final)


# length of string
x="Sarah"
len1=len(x)
print(len1)

y="Rajput"
len2=len(y)
print(len2)

concate=x + " " + y
print(concate)
print(len(concate))


# Indexing --- used to access characters of string, not change string character 
st="Sarah RJ"
print(st[2])
print(st[6])


# slicing --- accessing parts of string
# last character never add 
s1="Sarah Murtaza"
print(s1[1:4])  #ara (1-3)
print(s1[3:9])  #ah Mur (3-8)
print(s1[:5])  #Sarah
print(s1[6:])  #Murtaza
print(s1[6:len(s1)])  #Murtaza


# Negative Slicing
print(s1[-13:-8])  #Sarah
print(s1[-13:])  #Sarah Murtaza