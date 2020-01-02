# This program will print the number of trailing zeros the factorial
# of a number
# The formula and the associated explanations are available at:
# https://brilliant.org/wiki/trailing-number-of-zeros/

# Notes on the Python implementation are available on https://doingmathwithpython.github.io

import math
import matplotlib.pyplot as plt


def is_positive_integer(x):
    try:
        x = float(x)
    except ValueError:
        return False
    else:
        if x.is_integer() and x > 0:
            return True
        else:
            return False


def trailing_zeros(num):
    if is_positive_integer(num):
        # The above function call has done all the sanity checks for us
        # so we can just convert this into an integer here
        num = int(num)

        k = math.floor(math.log(num, 5))
        zeros = 0
        for i in range(1, k + 1):
            zeros = zeros + math.floor(num/math.pow(5, i))
        return zeros 
    else:
        print("Factorial of a non-positive integer is undefined")


if __name__ == "__main__":
    num_range = range(5, 10000, 10)
    zeros = []
    for num in num_range:
        num_zeros = trailing_zeros(num)
        zeros.append(num_zeros)
    for x, y in zip(num_range, zeros):
        print(x,y)
    plt.plot(num_range, zeros)
    plt.savefig('trailing_zeros.png')
