'''
henon.py

Plot 20,000 iterations of the Henon function
'''

import matplotlib.pyplot as plt

def transform(p):
    x,y  = p
    x1 = y + 1.0 - 1.4*x**2
    y1 = 0.3*x

    return x1, y1
     
if __name__ == '__main__':
    p = (0, 0)
    x = [p[0]]
    y = [p[1]]
    for i in range(20000):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])
    plt.plot(x, y, 'o')
    plt.show()
