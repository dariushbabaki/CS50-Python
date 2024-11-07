import random

user_input = 0
ai_choice = 0

while True:
    try:
        level = int(input("Please enter a positive integer for the game level: "))
            if level > 0:
                user_input = level
                ai_choice = random.randint(1,level)
                break
                
     except ValueError:
         pass
         
     except EOFError:
         print("\r")
         break
         
while True:
     try:
         user_guess = int(input("Guess your desired number: "))
         if user_guess == ai_choice:
             print("Just right!")
             break
         elif user_guess > ai_choice:
             print("Too large!")
         elif user_guess < ai_choice:
             print("Too small!")
      
     except ValueError:
         pass
