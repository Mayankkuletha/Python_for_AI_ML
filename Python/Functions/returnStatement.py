# return --> statement used to end a function and send a result back to the caller

# def add(x,y):
#     z = x+y
#     return z
# def substract(x,y):
#     z = x-y
#     return z
# def multiply(x,y):
#     z = x*y
#     return z

# print(add(15,20))
# # print(35) it will become like this.
# print(substract(15,20))
# print(multiply(15,20))


def create_userName(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_userName("mayank","kuletha")
print(full_name)