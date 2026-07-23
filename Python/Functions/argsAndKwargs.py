# *args = allows you to pass multiple non key arguments.   packs in tuples
# **kwargs=allows you to pass multiple keyword arguments.  packs in dictionary
# *unpacking operator

def add(*args):
    print(type(args))
    total =  0 
    for arg in args :
        total = total + arg
    return total

print(add(1,2,3,4))

def display_name(*args):
    for arg in args:
        print(arg,end=" ")

display_name("DR","Mayank","Kuletha")


# kwargs
def printing_address(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} : {value}")

printing_address(street = "123" , apt="100",city = "detroit",state="MI",zip = "54321")



# exercize

def shipping_label(*args, **kwargs):
    # Print full name using args
    for arg in args :
        print(arg , end = " ")
    print()
    # Print address using kwargs
    print(f"{kwargs.get('street')} {kwargs.get('city')} {kwargs.get('state')}{kwargs.get('zip')}")


shipping_label(
    "Mr.",
    "Mayank",
    "Kuletha",
    street="ABC Road",
    city="Delhi",
    state="Delhi",
    zip="110001"
)