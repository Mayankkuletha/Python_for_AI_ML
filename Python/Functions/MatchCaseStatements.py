# Match-Case Statements (switch) --> An alternative to using many elif.
# Execute some code if a  value matches a case.
# Benefits : Cleaner and syntax is more readable.

# def day_of_week(day):
#     match day:
#         case 1:
#             return "It is sunday"
#         case 2:
#             return "It is monday"
#         case 3:
#             return "It is tuesday"
#         case 4 :
#             return "It is wednesday"
#         case 5 :
#             return "It is thursday"
#         case 6:
#             return "It is Friday"
#         case 7 :
#             return "It is saturday"
#         case _:
#             return "not an valid day"

# day = int(input("enter the number which you want to check day"))
# print(day_of_week(day)) 

# example 2 we can also use or opeator (|) if many cases return same values
def day_of_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
            return False
        case _:
            return "not an valid day"

day = (input("enter the day which you want to check if its a weekend day"))
print(day_of_weekend(day)) 