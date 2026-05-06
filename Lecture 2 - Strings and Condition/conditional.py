# conditions
if(True):
  print("You can vote")  #indentation --- 4 tab spaces must occur
else:
  print("Cannot vote")  
  
  
  
age=20
if(age>=18):
  print("You can drive")
  print("You are young")
  
  
  
# if-elif statement
light="green"
if(light=="red"):
  print("stop")
elif(light=="green"):
  print("go")
elif(light=="yellow"):
  print("look")
else:
  print("Nothing happen")
  
print("end")  # always print





# marks=85
marks=int(input("Enter marks: "))
if(marks>=90 and marks<=100):
  grade="A"
elif(marks>=80 and marks<90):
  grade="B"
elif(marks>=70 and marks<80):
  grade="C"
elif(marks>=60 and marks<70):
  grade="D"
else:
  grade="F"
  
print("Your grade:",grade)




# Nested if-elif statements
age=57
if(age>=18):
  if(age>=60):
    print("cannot vote and drive")
  else:
    print("can drive")
else:
  print("cannot drive")