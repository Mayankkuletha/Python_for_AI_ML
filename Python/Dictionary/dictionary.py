# Dictionary --> a collection of key values pairs
# ordered and changeable , No duplicates

capitals = {"USA":"Washington D.C",
            "India":"New Delhi",
            "China" : "Bejing",
            "Russia":"Moscow"
            }

# print(dir(capitals)) 
# print(help(capitals))


# this will return the value of the key if no value then returns None
print(capitals.get("USA"))

# in this we can apply if else loop in dictionary and checks if exist or not
if capitals.get("Japan"):
    print("Exists in DB")
else:
    print("Not exist in DB")


# we can insert new key value pair or update the value of keys using update method 
capitals.update({"Germany" : "Berlin"})
print(capitals)
capitals.update({"USA":"Meow"})
print(capitals)

# will remove the key
capitals.pop("China")
print(capitals)

# will remove the latest key that has been added
capitals.popitem()
print(capitals)

# will print all the keys of the dictionary.
print(capitals.keys())

for key in capitals.keys():
    print(key)

# will print all the values of keys in a dictionary
print(capitals.values())

for value in capitals.values():
    print(value)


# items returns a dictionary object which resembles a 2D List of tupples , Its 
# will give u both keys and values
print(capitals.items())
for key,value in capitals.items():
    print(f"{key} , {value}")

print(capitals.clear())