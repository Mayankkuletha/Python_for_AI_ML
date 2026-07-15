# indexing = accesing elements of sequence using []->(set squares brackets)
# [start : end : step]


credit_number = "1234-5668-8888"
# print(credit_number[1]) #will give 2 
# print(credit_number[0:4]) # from 0 to 4 means starting 4 
# print(credit_number[:4]) #same as above
# print(credit_number[5:9])#from 5 to 9 means 5678 will not include last one
# print(credit_number[5:])#after 5th index all will be printed
# print(credit_number[-2])#2 last index
# print(credit_number[::3])#all with a gap of 3 each

# just print last 4 digits of a credit card number
# last_4_digit=credit_number[-4:]
# print(f"XXXX-XXXX-{last_4_digit}")

# if we want to reverse the whole credit number
credit_number = credit_number[::-1] # this will reverse the full credit_number
print(credit_number)