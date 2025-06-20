# choice- pick a random element from the list and return it and assigns it to word
from random import choice

def run_game():
    word:str = choice(['apple','secret', 'banana'])
    
    username :str = input('What is your name? ')
    print(f'Welcome to hangman, {username}')
    
    #setup
    guessed: str = ''
    tries : int = 3
    
    while tries >0:
        blank :int = 0
        
        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blank+=1
                
        print()#adds a blank line
        
        if blank == 0:
            print('You got it!')
            break
        
        guess : str = input('Enter a letter: ')
        
        if guess in guessed and len(guess)==1:
            print(f' You already used: {guess}. Try again\n')
        guessed += guess
        
        if guess not in word and len(guess)==1:
            tries -=1 
            print(f' Sorry, that was wrong. {tries} remain.\n')
            
            if  tries ==0:
                print ('No more tries remaing, sorry\n')
                break
        else:
            print('Please enter 1 letter.\n')
if __name__ == '__main__':
    run_game()