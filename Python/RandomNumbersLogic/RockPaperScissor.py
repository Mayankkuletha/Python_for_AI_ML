#A Rock paper scissor game
import random
options = ("rock" , "paper" , "scissor")

running = True
while running:
    player=None
    computer = random.choice(options)

    while player not in options :
        player =  input(" please choose one from rock , paper and scissor")

    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if player == "rock" and computer =="scissor":
        print("you won")
    elif player=="paper" and computer == "rock":
        print("you won")
    elif player == "scissor" and computer=="paper":
        print("You won")
    elif player==computer:
        print("Its a tie")
    else:
        print("You Loose!")

    
    play_again= input("want to play again (Y/N)").lower()
    if play_again!="y":
        running=False

print("thanku for Playing")
