# MemberShip Operators = used to test whether a value or variable is found in a sequence 
# (string , list, tuple , set or dictionary)
# 1.in
# 2.not in

# example strings
# word  = "apple"
# letter = input("enter the letter")
# if letter in word:
#     print("letter exists")
# else :
#     print("letter not in")

# example set
# students ={"Mayank" , "Himanshu" , "kartik" , "karan" ,"tushar"}
# name = input("enter the name you want to check ")

# if name not in students:
#     print(f"name {name} does not exist")
# else:
#     print(f"{name} name exists ")

# example dictionary
grades = {
    "Sandy":"A",
    "Maya":"B",
    "Shruti":"A",
    "Aman":"C"
}

students=input("Enter the name of Student")
if students in grades:
    print(f"{students} grade is {grades[students]}")
else:
    print(f"{students} is not found")


# # example
# email = "mayank@gmail.com"

# if "@" in email and "." in email:
#     print("valid email")
# else :
#     print("invalid email")