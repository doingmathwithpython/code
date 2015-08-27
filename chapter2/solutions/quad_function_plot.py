'''
quad_function_plot.py

Plot a Quadratic function 
'''

import matplotlib.pyplot as plt

def draw_graph(x, y):
    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    # assume values of x
    x_values = range(-100, 100, 20)
    y_values = []
    for x in x_values:
        # calculate the value of the quadratic
        # function
        y_values.append(x**2 + 2*x + 1)
    draw_graph(x_values, y_values)
