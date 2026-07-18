# A shopping Cart Program

# using list because tuples cannot be changed and set is unordered.
foods=[]
prices=[]
total = 0
while True :
    food = input("enter the food u want to add in cart  press q or Q for exit")
    if food.lower()=="q":
        break
    else:
       price= float(input(f"enter the price for your {food}: $"))
       foods.append(food)
       prices.append(price)

print("Your Cart!!!!!!!!")
for food in foods:
    print(food ,end=" ")

print()
for price in prices :
    total = total + price

print(f"the total of your cart item is ${total}")

