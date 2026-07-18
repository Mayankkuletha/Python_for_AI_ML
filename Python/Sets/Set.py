#set = {} unordered and immutable , but Add/remove ok , no duplicates

fruits={"apples","coconut","orange","banana","coconut"}
# print(dir(fruits))
print(len(fruits))
print("pineapple" in fruits)

fruits.add("pineapple") #adds pineapples in tuples
fruits.remove("apples") #removes the value of apple
# fruits.clear() #clears all the values of set

print(fruits)
