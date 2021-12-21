import random_walk_in_two_dimenions

steps = int(input("enter number of steps "))
number_of_particles = int(input("enter number of particles "))
paths = ()
for i in range(number_of_particles):
    paths.append(create_single_particle_diffusion(steps))

# fig is the figure object on which we draw our function
# chartfunc is the timeseries function that we graphs
# interval is the time delay  in ms
animator = ani.FuncAnimation(fig, chartfunc, interval = 100)
