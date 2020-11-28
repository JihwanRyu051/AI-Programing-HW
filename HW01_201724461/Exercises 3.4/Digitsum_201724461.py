def digit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = int(n/10)
    return sum

total = 0
for number in range(1, 3000001):
    total += digit(number)

print("The sum of the digits in the numbers from one million to three million is {0:,}.".format(total))
