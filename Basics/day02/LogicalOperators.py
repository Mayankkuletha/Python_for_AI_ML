# logical operators

# or --> any one should be true 
# temp = 25
# isRaining = True
# if temp>35 or temp<0 or isRaining :
#     print("the schedule is not perfect for today")
# else:
#     print("the schedule is perfect for today") 



# And --> all values should be true
# temp = 25
# isRaining = True
# if temp>35 and temp<0 and isRaining :
#     print("the schedule is not perfect for today")
# else:
#     print("the schedule is perfect for today") 

# NOT --> Inverts the condition (not False , not True)
temp = 20
isRaining = True
if temp>10 and not isRaining:
    print("no u can go")

else:
    print("you can go")