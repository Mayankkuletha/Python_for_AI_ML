# default arguments = A default value for certain parameters default is used when that argument is omitted make your functions more flexible .

# def net_price(list_price , discount , tax):
#     return list_price*(1-discount)*(1+tax)

# # it will show error if u will only pass one argument so for others we provide default values
# print(net_price(500))



def net_price(list_price , discount=0, tax=0.05):
    return list_price*(1-discount)*(1+tax)


print(net_price(5000))


import time
# this will show error because non default argument follows default arguments means non default should be written earlier.
# def count(start=0,end):
def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done!")

print(count(10,8))