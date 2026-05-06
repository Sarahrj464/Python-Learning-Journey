# store word meaning in dict

dict = {
  "table": [
    "a piece of furniture",
    "list of facts & figures"
  ],
  "cat":"a small animal",
}
print(dict)

 

# how many classrooms are needed
subjects = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(subjects))



dictionary = {}
marks1=int(input("Enter marks of subject 1: "))
marks2=int(input("Enter marks of subject 2: "))
marks3=int(input("Enter marks of subject 3: "))
dictionary["English"]=marks1
dictionary["Science"]=marks2
dictionary["Math"]=marks3
print(dictionary)

 
# 2nd method
marks = {}
a=int(input("Enter marks of subject 1: "))
marks.update({"math":a})
b=int(input("Enter marks of subject 2: "))
marks.update({"science":b})
c=int(input("Enter marks of subject 3: "))
marks.update({"phy":c})
print(marks)



# store 9 and 9.0 as separate values in set
myset = {9,'9.0'}
print(myset)

# sets elements -- immutable
# tuple -- immutable
# we cannot add dict to our sets
# so we store elements in a set using tuple
values  = {
  ("int",9),
  ("float",9.0)
}
print(values)