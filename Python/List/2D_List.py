# 2D list --> a list inside another list

# fruits=["apple", "banana","orange"]
# vegetables=["celery","carrots","potatoes"]
# nonveg=["chicken", "fish" ,"turkey"]

# groceries = [fruits,vegetables,nonveg]

# for collection in groceries:
#     # print(collection)
#     print(collection[0])

groceries = [["apple", "banana","orange"],["celery","carrots","potatoes"],["chicken", "fish" ,"turkey"]]
for collection in groceries:
    for food in collection:
      print(food,end=" ")
      print()


# similarly you can create 2D list and 2D tuple and 2D sets