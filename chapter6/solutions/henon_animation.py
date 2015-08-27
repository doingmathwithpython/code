'''
henon_animation.py

Animating 20000 iterations of the Henon function

'''

import matplotlib.pyplot as plt
from matplotlib import animation

def transform(p):
    x,y  = p
    x1 = y + 1.0 - 1.4*x**2
    y1 = 0.3*x

    return x1, y1

def update_points(i, x, y, plot):
    plot.set_data(x[:i], y[:i])
    return plot,
    
if __name__ == '__main__':
    p = (0, 0)
    x = [p[0]]
    y = [p[1]]
    for i in range(10000):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])

    fig = plt.gcf()
    ax = plt.axes(xlim = (min(x), max(x)),
                  ylim = (min(y), max(y)))
    plot = plt.plot([], [], 'o')[0]
    anim = animation.FuncAnimation(fig, update_points,
                                   fargs=(x, y, plot),
                                   frames = len(x),
                                   interval = 25)
    plt.title('Henon Function Animation')
    plt.show()
