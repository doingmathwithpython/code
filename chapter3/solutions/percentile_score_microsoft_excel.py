'''
percentile_score_microsoft_excel.py

Calculate the number from a list of numbers which corresponds 
to a specific percentile

This implements the "Microsoft Excel Method":
https://en.wikipedia.org/wiki/Percentile#Microsoft_Excel_method

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
    rank = (percentile/100)*(n-1) + 1
    k = int(rank)
    d = rank - k

    real_idx_1 = k-1
    real_idx_2 = k

    return data[real_idx_1] + d*(data[real_idx_2]-data[real_idx_1])

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
