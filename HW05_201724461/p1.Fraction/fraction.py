class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self._numerator = numerator
        self._denominator = denominator

    def setNumerator(self, numerator):
        self._numerator = numerator

    def setDenominator(self, denominator):
        self._denominator = denominator

    def getNumerator(self, numerator):
        return self._denominator

    def getDenominator(self, denominator):
        return self._denominator

    def GCD(self, numerator, denominator):
        while denominator != 0:
            t = denominator
            denominator = numerator % denominator
            numerator = t
        return numerator

    def __str__(self):
        gcd = self.GCD(self._numerator, self._denominator)
        return (str(int(self._numerator/gcd)) +"/" + str(int(self._denominator/gcd)))
