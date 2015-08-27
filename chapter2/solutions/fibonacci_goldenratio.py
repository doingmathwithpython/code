'''
fibonacci_goldenration.py

Relationship between Fibonacci sequence and Golden ratio
'''

import matplotlib.pyplot as plt

def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    # n > 2
    a = 1
    b = 1
    # first two members of the series
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c

    return series

def plot_ratio(series):
    ratios = []
    for i in range(len(series)-1):
        ratios.append(series[i+1]/series[i])
    plt.plot(ratios)
    plt.title('Ratio between Fibonacci numbers & Golden ratio')
    plt.ylabel('Ratio')
    plt.xlabel('No.')
    plt.show()

if __name__ == '__main__':
    # Number of fibonacci numbers
    num = 100
    series = fibo(num)
    plot_ratio(series)
