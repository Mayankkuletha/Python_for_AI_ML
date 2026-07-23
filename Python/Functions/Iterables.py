# Iterables = an object/collection that can return its element one at a time.
# allowing it to be iterated over in a loop

# list are iterables
myList=["1,2,3,4,5"]
for list in myList:
    print(list,end = " ")
print()

# tuples are iterables
myList=("1,2,3,4,5")
for list in myList:
    print(list,end = " ")
print()


# sets  are iterables
myList={"1,2,3,4,5"}
for list in myList:
    print(list,end = " ")
print()
    
# strings are iterable
str = "Bro Code"
for chr in str :
    print(chr,end = " ")
print()

myDic={"name" :"aman", "age":20 ,"rollno":21}
for keys,values in myDic.items():
    print(f"{keys}={values}")
print()