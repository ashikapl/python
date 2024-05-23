# Create a terminal based Rock, Paper and Scissor Game using random(module)
# Game btwn computer and a user
import random

options = ('rock','paper','scissor')
running = True

while running:
    
    player = None
    computer = random.choice(options)
    
    while player not in options:
        
        player = input("Select one option: (rock, paper or scissor): ")
        
    print(f"player select: {player}")
    print(f"Computer select: {computer}")
        
    if player == computer:
        print("It's Tie..!")
            
    elif player == "rock" and computer == "scissor":
        print("You win..!")
            
    elif player == "paper" and computer == "Rock":
        print("You win..!") 
            
    elif player == "scissor"  and computer == "paper":
        print("You win..!")
        
    else:
         print("You lose..!")

    play_again = input("You want to play again?: (y/n)").lower()
        
    if not play_again == 'y':
        running = False
        
print("Thank You for Playing...!")