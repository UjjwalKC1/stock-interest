Amount = int(input("Enter the amount: "))
# Enter the number of years
Year = int(input("Enter the number of years: "))

# Enter the rate of interest
Rate = float(input("Enter the rate of interest: "))
t = 0
for x in range(Year):
    interest = (Amount*Rate)/100
    Amount = Amount+interest
    t = t+1
    print("the interest of the amount in", t, Amount)
