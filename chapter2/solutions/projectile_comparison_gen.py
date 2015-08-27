"""

projectile_comparison_gen.py

Compare the projectile motion of a body thrown with various combinations of initial 
velocity and angle of projection.
"""

import matplotlib.pyplot as plt
import math

g = 9.8

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion at different initial velocities and angles')
    
def frange(start, final, interval):

    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval
    
    return numbers

def draw_trajectory(u, theta, t_flight):
    # list of x and y co-ordinates
    x = []
    y = []
    intervals = frange(0, t_flight, 0.001)
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)

    #create the graph
    draw_graph(x, y)

if __name__ == '__main__':

    num_trajectories = int(input('How many trajectories? '))
    
    velocities = []
    angles = []
    for i in range(1, num_trajectories+1):
        v = input('Enter the initial velocity for trajectory {0} (m/s): '.format(i))
        theta = input('Enter the angle of projection for trajectory {0} (degrees): '.format(i))
        velocities.append(float(v))
        angles.append(math.radians(float(theta)))

    for i in range(num_trajectories):
        # calculate time of flight, maximum horizontal distance and
        # maximum vertical distance
        t_flight = 2*velocities[i]*math.sin(angles[i])/g
        S_x = velocities[i]*math.cos(angles[i])*t_flight
        S_y = velocities[i]*math.sin(angles[i])*(t_flight/2) - (1/2)*g*(t_flight/2)**2
        print('Initial velocity: {0} Angle of Projection: {1}'.format(velocities[i], math.degrees(angles[i])))
        print('T: {0} S_x: {1} S_y: {2}'.format(t_flight, S_x, S_y))
        print()
        draw_trajectory(velocities[i], angles[i], t_flight)
        
    # Add a legend and show the graph
    legends = []
    for i in range(0, num_trajectories):
        legends.append('{0} - {1}'.format(velocities[i], math.degrees(angles[i])))
    plt.legend(legends)
    plt.show()
