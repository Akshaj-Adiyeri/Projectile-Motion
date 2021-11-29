import math, numpy, matplotlib.pyplot

h = 0.001 # small time interval
g = -9.81 # m / s2
acceleration = numpy.array([0., -g])
initial_speed = 20. # m / s

def trajectory():
    angles = numpy.linspace(20., 70., 25)

    for angle in angles:
        angle_rad = angle * math.pi/180
        ToF = -2 * math.sin(angle_rad) * initial_speed / g # Time of flight
        time_steps = int(ToF//h)
        x = numpy.zeros([time_steps + 1, 2])
        v = numpy.zeros([time_steps + 1, 2])
        v_horizontal = initial_speed * math.cos(angle_rad)
        v_vertical = initial_speed * math.sin(angle_rad)
        v[:,0] = v_horizontal
        v[0,1] = v_vertical
        counter = 0
        while counter < time_steps:
            x[counter + 1,0] = x[counter,0] + v_horizontal * h
            v[counter + 1,1] = v[counter,1] + g * h 
            x[counter + 1,1] = x[counter,1] + v[counter,1] * h
            counter += 1 
        
        matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.axis('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Horizontal position in m')
    axes.set_ylabel('Vertical position in m')
    return x, v

a=[0,45]
b=[0,0]
matplotlib.pyplot.plot(a,b)
trajectory()
matplotlib.pyplot.show()