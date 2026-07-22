import random 

# randint for random integer whole number
# we can also write direct values inside rather than variables
# low = 1 
# high = 8
# number = random.randint(low,high)
# print(number)

# for random floating number
# numbers = random.random()
# print(numbers)

# if we have to choose some random choice from options
options = ("rock" , "paper" , "scissors")
choose = random.choice(options)
print(choose)

cards = [1,2,3,4,5,6,7,8,9,"A","K","Q","J"]
random.shuffle(cards)
print(cards)