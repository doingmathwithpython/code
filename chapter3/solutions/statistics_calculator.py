'''
statistics_calculator.py

Read numbers from a file, calculate and print statistical measures:
mean, median, mode, variance, standard deviation
'''

from stats import mean, median, mode, variance_sd

def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))

    return numbers

if __name__=='__main__':
    data = read_data('mydata.txt')
    m = mean(data)
    median = median(data)
    mode = mode(data)
    variance, sd = variance_sd(data)
    print('Mean: {0:.5f}'.format(m))
    print('Median: {0:.5f}'.format(median))
    print('Mode: {0:.5f}'.format(mode))
    print('Variance: {0:.5f}'.format(variance))
    print('Standard deviation: {0:.5f}'.format(sd))
