import math

def calculuate_e(precision):
    result = 0
    for i in range(precision+4):
        factorial = math.factorial(i)
        num_e = 1/factorial
        result = num_e + result
    return round(result,precision)

precision = int(input("How many decimal points of accuracy do you want for the calculation of e? "))
print("e is approximately",calculuate_e(precision))
