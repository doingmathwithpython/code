'''
estimate_circle_area.py

Estimate the area of a circle
'''
import math
import random

def estimate(radius, total_points):
    center = (radius, radius)

    in_circle = 0
    for i in range(total_points):
        x = random.uniform(0, 2*radius)
        y = random.uniform(0, 2*radius)
        p = (x, y)
        # distance of the point created from circle's center
        d = math.sqrt((p[0]-center[0])**2 + (p[1]-center[1])**2)
        if d <= radius:
            in_circle += 1
    area_of_square = (2*radius)**2
    return (in_circle/total_points)*area_of_square

if __name__ == '__main__':
    radius = float(input('Radius: '))
    area_of_circle = math.pi*radius**2
    for points in [10**3, 10**5, 10**6]:
        print('Area: {0}, Estimated ({1}): {2}'.format(area_of_circle, points, estimate(radius, points)))
