'''
grouped_frequency.py

Create a grouped frequency table from a list of numbers
'''

def create_classes(numbers, n):
    low = min(numbers)
    high = max(numbers)

    # width of each class
    width = (high - low)/n
    classes = []
    a = low
    b = low + width
    classes = []
    while a < (high-width):
        classes.append((a, b))
        a = b
        b = a + width
    # The last class may be of size
    # less than width
    classes.append((a, high+1))
    return classes

def classify(numbers, classes):
    # Create a list with the same number of elements
    # as the number of classes
    count = [0]*len(classes)
    for n in numbers:
        for index, c in enumerate(classes):
            if n >= c[0] and n < c[1]:
                count[index] += 1
                break
    return count

def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
    return numbers

if __name__ == '__main__':
    
    num_classes = int(input('Enter the number of classes: '))
    numbers = read_data('marks.txt')
    
    classes = create_classes(numbers, num_classes)
    count = classify(numbers, classes)
    for c, cnt in zip(classes, count):
        print('{0:.2f} - {1:.2f} \t {2}'.format(c[0], c[1], cnt))
