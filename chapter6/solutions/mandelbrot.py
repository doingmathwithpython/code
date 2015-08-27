'''
mandelbrot.py

Draw a Mandelbrot set

Using "Escape time algorithm" from:
http://en.wikipedia.org/wiki/Mandelbrot_set#Computer_drawings

Thanks to http://www.vallis.org/salon/summary-10.html for some important
ideas for implementation.

'''
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Subset of the complex plane we are considering
x0, x1 = -2.5, 1
y0, y1 = -1, 1

def initialize_image(x_p, y_p):
    image = []
    for i in range(y_p):
        x_colors = []
        for j in range(x_p):
            x_colors.append(0)
        image.append(x_colors)
    return image

def mandelbrot_set():
    # Number of divisions along each axis
    n = 400
    # Maximum iterations
    max_iteration=1000
    
    image = initialize_image(n, n)
    
    # Generate a set of equally spaced points in the region
    # above
    dx = (x1-x0)/(n-1)
    dy = (y1-y0)/(n-1)
    x_coords = [x0 + i*dx for i in range(n)]
    y_coords = [y0 + i*dy for i in range(n)]

    for i, x in enumerate(x_coords):
        for k, y in enumerate(y_coords):
            z1 = complex(0, 0)
            iteration = 0
            c = complex(x, y)
            while (abs(z1) < 2  and iteration < max_iteration):
                z1 = z1**2 + c
                iteration += 1
            image[k][i] = iteration
    return image

if __name__ == '__main__':
    image = mandelbrot_set()
    plt.imshow(image, origin='lower', extent=(x0, x1, y0,y1),
               cmap=cm.Greys_r, interpolation='nearest')
    plt.show()
