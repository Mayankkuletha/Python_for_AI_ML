# ternary operator --> a one line shortcut for the if-else statement(ternary opeartor)
#  X if condition else Y

age = 18
voting = "voting right given" if age >=18 else "no rights are given u are too young for it"
role = "guest"
acess = "full acess granted " if role == "admin" else "limited acess"
print(acess)