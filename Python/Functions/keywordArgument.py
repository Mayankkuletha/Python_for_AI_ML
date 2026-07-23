# keyword arguments = an argument preceded by an identifier
# helps with readablity
# order of argument doesn't matter

def hello(greeting , title , first , last) :
    print(f"{greeting} {title} {first} {last}")

# # positional should be ahead of keyword arguments.
hello("hello" , title="mr." , first="john" , last="james")


# # end is also a keyword argument
for x in range(1,10):
    print(x , end = " ")

# sep is a  keyword argument that is used to seprate things using diffrent things.

print(1,2,3,4,5 , sep=".")

def get_phone(country , area , first , last) :
    return f"{country} - {area}-{first}-{last}"

phone_num = get_phone(1,123,456,7890)

print(phone_num)