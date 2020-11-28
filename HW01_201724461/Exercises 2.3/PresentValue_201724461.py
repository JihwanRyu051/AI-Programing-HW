future = float(input("Enter future value: "))
rate = float(input("Enter interest rate (as %): "))
year = float(input("Enter number of years: "))

present = future / ((1+rate*0.01)**year)

print("${0:5,.2f}".format(present))
print("Done")
