import random

# (->) ; is return
def roll_dice(amount: int = 2)-> list[int]:
    if amount<= 0:
        raise ValueError
    
    rolls: list[int]= []
    for i in range(amount):
        random_roll: int = random.randint(1,6)
        rolls.append(random_roll)
        # if you need to get some value, add it to the return value
    return rolls, sum(rolls)

def main():
    while True:
        try:
            user_input :int = input("How many dice would you like to roll or exit? ")
            
            if user_input.lower()== 'exit':
                print("Thank you for playing")
                break
            # (*) unpack the list;
            rolls, total = roll_dice(int(user_input))
            print(*rolls , sep=', ')
            print(f"Total: {total}")
            
        except ValueError:
            print('Please enter a valid number')
            
if __name__== '__main__':
    main()
    