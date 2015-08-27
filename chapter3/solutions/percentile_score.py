'''
percentile_score.py

Calculate the number from a list of numbers which corresponds 
to a specific percentile.

This implements the method described at 
http://web.stanford.edu/class/archive/anthsci/anthsci192/anthsci192.1064/handouts/calculating%20percentiles.pdf
'''

def find_percentile_score(data, percentile):
    if percentile < 0 or percentile > 100:
        return None
    data.sort()
    if percentile == 0:
        return data[0]
    if percentile == 100:
        return data[-1]
    n = len(data)
    i = ((n*percentile)/100) + 0.5

    if i.is_integer():
        real_idx = int(i-1)
        return data[real_idx]
    else:
        k = int(i)
        f = i - k
        real_idx_1 = k - 1
        real_idx_2 = k 
        return (1-f)*data[real_idx_1] + f*data[real_idx_2]

def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
    return numbers

if __name__ == '__main__':
    percentile = float(input('Enter the percentile score you want to calculate: '))
    data = read_data('marks.txt')
    percentile_score = find_percentile_score(data, percentile)
    if percentile_score:
        print('The score at {0} percentile: {1}'.format(percentile, percentile_score))
    else:
        print('Could not find the score corresponding to {0} percentile'.format(percentile))
