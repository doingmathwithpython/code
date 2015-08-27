'''
estimate_pi.py

Estimate the value of Pi
'''
import math
import random

def estimate(total_points):
    radius = 1
    center = (radius, radius)

    in_circle = 0
    for i in range(total_points):
        x = random.uniform(0, 2*radius)
        y = random.uniform(0, 2*radius)
        p = (x, y)
        # distance from circle's center
        d = math.sqrt((p[0]-center[0])**2 + (p[1]-center[1])**2)
        if d <= radius:
            in_circle += 1
    return (in_circle/total_points)*4

if __name__ == '__main__':
    for points in [10**3, 10**5, 10**6]:
        print('Known value: {0}, Estimated ({1}): {2}'.format(math.pi, points, estimate(points)))
