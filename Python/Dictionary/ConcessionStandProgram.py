# Concession Stand Program
menu ={
    "pizza":3.00,
    "maggi":5.2,
    "samosa":2.0,
    "sweets":5.0,
    "icecream":2.25,
}

cart=[]
total = 0 

#Menu
print("------MENU------------XXX")
for key,value in menu.items():
    print(f"{key} , {value}")
print("-------------------------")

# Taking Input from user
while True:
   food =  input("Enter the item you want to order , Q or q for quit").lower()
   if food=="q":
        break
   elif menu.get(food) is not None:
      cart.append(food)

print("-------------Your Items ----------------")
for food in cart:
    total = total + menu.get(food)
    print(food,end=" ")

print()
print(f"The total of our food is {total:2f}")