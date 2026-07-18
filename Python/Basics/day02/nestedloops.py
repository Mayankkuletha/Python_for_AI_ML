# nested loop = A loop within another loop(outer,inner)
#  outer loop :
    # inner loop :

# for x in range(3):
#     for y in range(1,10):
#         print(y,end="") #end here means all will be in line without space default will be next line so we can do many things with end = something (dash , empty string etc).
#     print()


#now lets make an rectangle with symbols

rows = int (input("enter the number of rows"))
columns = int (input("enter the number of columns"))
symbol= input("enter the symbol you want to use")

for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print()