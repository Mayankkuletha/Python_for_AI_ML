# we will make a weight calculator program
weight = float(input("enter the weight of yours"))
unit = input("Kilograms or Pounds? (K or L)")
if unit=="K":
    weight = weight * 2.025
    unit = "Lbs"
    print(f"the weight is {round(weight,1)}")

elif unit == "L" :
    weight = weight / 2.205
    unit = "kgs."
    print(f"weight is {round(weight,1)}") 
else:
    print(f"invalid {unit}")