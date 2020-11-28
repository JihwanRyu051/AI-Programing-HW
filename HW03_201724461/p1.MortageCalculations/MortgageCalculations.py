def main():
    interest = 0
    payment = 0
    mbalance = 0
    tup = Input()
    cal = Calculate(tup)
    Output(cal)


def Input():
    interest = float(input("Enter annual rate of interest: "))
    payment = float(input("Enter monthly payment: "))
    mbalance = float(input("Enter beg. of month balance: "))
    tup = [interest, payment, mbalance]
    return tup


def Calculate(tup):
    interestformonth = tup[2]*0.05 / 12
    reduction = tup[1] - interestformonth
    endbalance = tup[2] - reduction
    cal = [interestformonth, reduction, endbalance]
    return cal


def Output(cal):
    print("Interest paid for the month: ${0:,.2f}".format(cal[0]))
    print("Reduction of principal: ${0:,.2f}".format(cal[1]))
    print("End of month balance: ${0:,.2f}".format(cal[2]))


main()

