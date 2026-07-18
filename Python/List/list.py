#List --> ordered and changeable . Duplicates Ok
fruits = ["apples" , "mango" , "orange" , "banana", "coconut" ]
# print(fruits[0])
# for fruit in fruits:
#     print(fruit , end = " ")

# all methods of list
# print(dir(fruits))
# print(help(fruits))

# some list functions
print(len(fruits)) #length of a list
print("pinneapple" in fruits) #element is in the list or not.
# fruits[0]= "pineapple" #means the list is changeable
# fruits.append("pineapple") # adds at last
# fruits.remove("coconut") #will remove the element
# fruits.insert(0,"pinneapple") #will insert an element
fruits.sort() #will sort the list
fruits.reverse() #will reverse the list
# fruits.clear() #will clear the list
print(fruits.index("apples"))#will give you the index of that element.
print(fruits)


