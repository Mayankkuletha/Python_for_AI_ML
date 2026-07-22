# Python Random Number Guessing Game 
import random
low_number=1
high_number=100
answer = random.randint(low_number,high_number)
print("Python Random Number Guessing Game")
guesses = 0
isRunning = True

while isRunning:
    guess = input("enter the number")
    if guess.isdigit():
        guess = int(guess)
        guesses+=1
        if guess<low_number or guess>high_number:
          print(f"enter the valid number between {low_number} and {high_number}")

        elif guess<answer:
            print("too low! please enter bigger number")

        elif guess>answer:
            print("too high please enter lower number")

        else :
            print(f"you gueesed the correct number the number was {answer}")
            print(f"you gueesed in {guesses} attempts")
            print("----------THANK YOU-------------")


    else:
        print("inavalid guess")
        print(f"enter the valid number between {low_number} and {high_number}")