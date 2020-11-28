def main():
    prime = []
    begin = 500
    end = 1000
    for n in range(begin, end+1):
        if isPrime(n):
            prime.append(n)
        if len(prime) > 9 or n == end:
            print(prime)
            prime.clear()



def factorial(n):
    fac = 1
    while n > 1:
        fac *= (n-1)
        n -= 1
    return fac+1


def isPrime(n):
    if factorial(n) % n == 0:
        return True
    else:
        return False


main()
