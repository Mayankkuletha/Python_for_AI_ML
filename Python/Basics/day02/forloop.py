# for loops --> execute a block of code a fixed number o ftimes.
# you can iterate over a range , string , sequence etc.

# last one will excluded so till 11.
for x in range (1,11) :
    print(x)

# for reverse printing
for x in reversed (range(1,11)) :
    print(x)

print("happy new year")

# range(1,11,2) 2 here is step means we have to print number in gap of 2 .

for x in range (1,11,2):
    print(x)

# break statement --> after that element no one will be printed
for x in range(1,11) :
    if x == 5 :
        break
    else:
        print(x)

# continue statement --> only skips that number and other will be printed
for x in range(1,11) :
    if x == 5 :
        continue
    else:
        print(x)


# without range
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
