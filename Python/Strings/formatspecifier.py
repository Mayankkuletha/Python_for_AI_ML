#format specifiers = {value:flags} formats a value based on what flags are interested

# .number(f)--> round to that many decimal places(fixed point)
# :(number)--> allocate that many spaces
# :03 --> allocate and zero pad that many spaces
# :< --> justify left 
# :> --> justify right
# :^ --> center align 
# :+ --> use a plus sign to indicate positive value
# :== place sign to leftmost position
# := insert a space before positive numbers
# :,= comma seprator

price = 3.14159
price1=-987.65

# upto that decimal values
# print(f"the price is {price :.2f}")
# print(f"the price1 is {price1:.2f}")


# that much spaces 
# print(f"the price is {price:50}")
# print(f"the price1 is {price1:3}")

# means space of 10 and all spaces padded up with zeros
# print(f"the price is {price :010}")
# print(f"the price1 is {price1:010}")


# justify content  towards left 
# print(f"the price is {price :<10}")
# print(f"the price1 is {price1 :<10}")


# justify content towards right
# print(f"the price is {price :>10}")
# print(f"the price1 is {price1 :>10}")



# align content towardscenter
# print(f"the price is {price :^10}")
# print(f"the price1 is {price1 :^10}")


# will assign positive sign to positive values negative will remain negative.
print(f"the price is {price :+}")
print(f"the price1 is {price1:+}")


# we can assign multiple format specifiers combinely
print(f"the price is {price :+,.2f}")
