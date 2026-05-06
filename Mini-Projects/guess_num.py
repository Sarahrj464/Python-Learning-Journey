import random

target=random.randint(1,100)

while True:
  
  userChoice=input("Guess the target or Quit(Q): ")
  
  if(userChoice=="Q"):
    break
  
  userChoice=int(userChoice)
  
  if(userChoice==target):
    print("Congrats!! You guessed the number")
    break
  elif(userChoice>target):
    print("The number is too large. Take smaller guess...")
  else:
    print("The number is too small. Take larger guess...")
  
print("--- GAME OVER ---")