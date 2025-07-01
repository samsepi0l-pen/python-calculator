principle = float(input("enter the principle amount: "))
rate = float(input("enter the interest rate: "))
time = int(input("enter the time in years: "))
while principle <= 0:
    print("principle amount cannot be equal to or less than zero")
    principle = float(input("enter the principle amount: "))

while rate <= 0:
    print("interest rate cannot be equal to or less than zero")
    rate = float(input("enter the interest rate: "))

while time <= 0:
    print("time cannot be equal to or less than zero")
    time = int(input("enter the time in years: "))

total = principle * pow((1 + rate / 100), time)
print(f"the balance after {time} years is ${round(total, 2)}")