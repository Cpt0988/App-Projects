# import the random lib.
from random import randint

#declare limits,random number,attempts & print user question
low, high = (1,10)
random_num : int = randint(low,high)
start: int = 4
print(f"Guess a number between {low} and {high}.")


def a():
   print(f"Attempts reminding: {start}") 
     
#loop with a limit of 4 guess, only accept number answers

while start > 0:
   
    start -= 1
    try:
        user_input: int = int(input("Guess: "))
    except ValueError as e:
        print("Use a number answer.")
        
    if user_input> random_num and start != 0:
        print('The number is lower.')
        a()
    elif(user_input< random_num and start != 0):
        print('The guess is higher.')
        a()
    
    elif(user_input == random_num):
        print(f"{user_input}, is correct!!")
        break
    
    else:
        print("You are out of attempts.")
        break
        
   
    