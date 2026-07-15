# Compund interest calculator
principle = 0 
rate = 0 
time = 0 

while principle <=0 :
    principle = float(input("enter the principle value"))
    if principle < 0 :
        print("principle cant be less than 0")
while rate <=0 :
    rate = float(input("enter the rate value"))
    if rate < 0 :
        print("rate cant be less than 0")
while time <=0 :
    time = float(input("enter the time "))
    if time < 0 :
        print("time cant be less than 0")

total = principle * pow((1 + rate / 100),time)
print(f" balance after {time} years is ${total :.2f}")