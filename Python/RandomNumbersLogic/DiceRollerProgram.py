import random

# Dice Faces
dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘",
    )
}

dice = []
total = 0

num_of_dice = int(input("How many dice?: "))

for i in range(num_of_dice):
    dice.append(random.randint(1, 6))

print()

# Print Dice
for line in range(5):
    for die in dice:
        print(dice_art[die][line], end=" ")
    print()

# print die in horizontal order
# for die range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#       print(line)


# Total
for die in dice:
    total += die

print(f"\nTotal: {total}")