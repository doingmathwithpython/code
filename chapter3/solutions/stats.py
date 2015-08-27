'''
stats.py

Python module with functions for calculating common statistical measures

'''
from collections import Counter

def mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N

    return mean

def median(numbers):
    # find the numnber of items
    N = len(numbers)

    # sort the list in ascending order
    numbers.sort()
    
    # find the median
    if N % 2 == 0:
        # if N is even
        m1 = N/2
        m2 = (N/2) + 1
        # convert to integer, match position
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2])/2
    else:
        m = (N+1)/2
        # convert to integer, match position
        m = int(m) - 1
        median = numbers[m]

    return median

def mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]

def find_differences(numbers):
    m = mean(numbers)
    # find the differences from the mean
    diff = []
    for num in numbers:
        diff.append(num-m)

    return diff

def variance_sd(numbers):
    # find the list of differences
    diff = find_differences(numbers)
    # find the squared differences
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    # find the variance
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(numbers)
    return variance, variance**0.5
