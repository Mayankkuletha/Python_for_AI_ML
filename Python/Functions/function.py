# function --> a block of reusable code
# place () after the function name to invoke it.

# def happy_birthday():
#     print("happy birthday to you")
#     print("you are 27 year old")
#     print("happy birthday once again!!!")

# happy_birthday()
# Parameters are the variables listed in the function definition.
def happy_birthday(name,age):
    print(f"happy birthday to you {name}")
    print(f"you are {age} year old")
    print("happy birthday once again!!!")
# Arguments are the actual values passed to the function when it is called.
happy_birthday("mayank",20)

# here 20 is the argument and name , age are parameters.

def display_invoice(username,amount,due_date):
    print(f"hello {username}")
    print(f"you bill of ${amount:2f} is due: {due_date}")

display_invoice("mayank",25000,"01/10/2025")