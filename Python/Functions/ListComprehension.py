# List Comprehension = A concise way to create lists in Python
# Compact and easier to read than traditional loops.
# [expression for value in iterable if condition]

# normal for loop to double a numbers
# doubles=[]
# for x in range(1,11):
#     x = x*2
#     doubles.append(x)
#     print(x , end = " ")

# we can reduce the code with the help of list comprehension method
doubles = [x*2 for x in  range(1,11)]
triples =[y*3 for y in range(1,11)]
squares = [z*z for z in range(1,11)]
print(doubles)
print(triples)
print(squares)


fruits = ["apples","banana","coconut"]
fruits=[fruit.upper() for fruit in fruits]
fruits_chars=[fru[0] for fru in fruits]
print(fruits)
print(fruits_chars)

numbers = [1,-2,3,8,10,12,4,-5,-6]
positive_num=[num for num in numbers if num>0]
print(positive_num)
neg_num = [num for num in numbers if num<0]
print(neg_num)
even_num = [num for num in numbers if num%2==0]
print(even_num)

grades=[85,55,22,95,75]
pass_grade=[grade for grade in grades if grade>60]
print(pass_grade)