from random import randint

lower_num, high_num =1, 10 
random_num :int = randint(lower_num,high_num)
print(f"Guess the number between {lower_num} and {high_num}")

while True:
    try:
       user_input : int =int(input('Guess: ')) 
    except ValueError as e:
        print('Please enter a valid number.')
        
    if user_input> random_num:
        print('The number is lower.')
    elif(user_input< random_num):
        print('The guess is higher.')
    else:
        print(f"{user_input}, is correct!!")
        break
    