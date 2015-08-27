'''
expenditures_barchart.py

Visualizing the weekly expenditure using a bar chart
'''

import matplotlib.pyplot as plt

def create_bar_chart(data, labels):
    # number of bars
    num_bars = len(data)
    # this list is the point on the y-axis where each
    # bar is centered. Here it will be [1, 2, 3..]
    positions = range(1, num_bars+1)
    plt.barh(positions, data, align='center')
    # set the label of each bar
    plt.yticks(positions, labels)
    plt.xlabel('Amount')
    plt.ylabel('Categories')
    plt.title('Weekly expenditures')
    # Turns on the grid which may assist in visual estimation
    plt.grid()
    plt.show()

if __name__ == '__main__':
    n = int(input('Enter the number of categories: '))
    labels = []
    expenditures = []
    for i in range(n):
        category = input('Enter category: ')
        expenditure = float(input('Expenditure: '))
        labels.append(category)
        expenditures.append(expenditure)
    create_bar_chart(expenditures, labels)
