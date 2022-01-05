import random_walk_in_two_dimensions
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
####################################################
import pdb
####################################################

steps = int(input("enter number of steps "))
#number_of_particles = int(input("enter number of particles "))
number_of_particles = 1
paths = []
for i in range(number_of_particles):
    paths.append(random_walk_in_two_dimensions.create_single_particle_diffusion(steps))
#we now have a list of lists of doubles representing time series paths

for path in paths:
    x_values = [item[0] for item in path]
    y_values = [item[1] for item in path]
    #t_values = [item[2] for item in path]


fig = plt.figure()

#axis = plt.axes(xlim =(-1*steps, steps), ylim =(-1*steps, steps))
axis = plt.axes(xlim =(-30, 30), ylim =(-30,30))

line, = axis.plot([], [], lw = 2)

# what will our line dataset
# contain?
def init():
    line.set_data([], [])
    return line,

# initializing empty values
# for x and y co-ordinates
xdata, ydata = [], []

# animation function
x_iterator = iter(x_values)
y_iterator = iter(y_values)

def animate(i):
    # t is a parameter which varies
    # with the frame number
    t = 0.1 * i

    # x, y values to be plotted
    x = next(x_iterator,None)
    y = next(y_iterator,None)

    # appending values to the previously
    # empty x and y data holders
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    axis.relim()
    axis.autoscale_view()

    return line,

# calling the animation function
anim = animation.FuncAnimation(fig, animate, init_func = init,frames = 500,interval = 20, blit = True)
plt.show()
mywriter = animation.FFMpegWriter(fps=60)
#anim.save('myanimation.mp4',writer=mywriter)
print("done")
