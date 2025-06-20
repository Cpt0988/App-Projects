import random
import sys

class RPS:
#initilizer take care of giving an intro screen
    def __init__(self):
        print('Welcome to RPS 9000')
        # make a dictatory
        self.moves : dict = {'rock':'🪨', 'paper': '📃','scissors':'✂️'}
        self.valid_move: list[str] =list(self.moves.keys())
        self.user_score : int = 0
        self.ai_score : int = 0
        self.tie_score : int = 0
        

    def play_game(self):
        use_move:str= input('Rock, paper or scissors?  >> '.lower())
        
        if use_move=='exit':
            print('Thank you for playing')
            sys.exit()
        
        if use_move not in self.valid_move:
            print('Invalid move...')
            return self.play_game()
        
        ai_move = random.choice(self.valid_move)
        
        self.display_move(use_move, ai_move)
        self.check_move(use_move, ai_move)
    
    def display_move(self, use_move: str, ai_move: str):
        
        print('----')
        print(f'You: {self.moves[use_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('----')
    
    def check_move(self, use_move: str, ai_move: str):
        if use_move == ai_move:
            print('Its a tie!')
            self.tie_score +=1
        elif use_move=='rock' and ai_move=='scissors':
            print('You win!!')
            self.user_score +=1
        elif use_move=='scissors' and ai_move=='paper':
            print('You win!!')
            self.user_score +=1
        elif use_move=='paper' and ai_move=='rock':
            print('You win!!')
            self.user_score +=1
        else:
            print('You lose!')
            self.ai_score +=1
        print(f'User:{self.user_score}-AI:{self.ai_score}-Tie:{self.tie_score}')
     

if __name__=='__main__':
    rps = RPS()
    while True:
        rps.play_game()