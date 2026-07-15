# validate user input exercise
# 1.username is no more then 12 characters.
# 2. username must not contain spaces.
# 3. username must not contain digits.

username = input("enter the username")

if len(username)>12 :
    print("username must conatin maximum of 12 characters")
elif not username.find(" ")==-1:
    print("username should not contain spaces")
elif not username.isalpha() :
    print("username should not contain digits")
else :
    print("username is valid")