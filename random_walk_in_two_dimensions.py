import random

steps = int(input("enter number of steps"))

def create_single_particle_diffusion(steps):
    # the probability that we move (or dont move) in any direction is equal
    prob_left, prob_right, prob_up, prob_down, prob_stay = .25

    # create a list of pairs representing position in x and y at time t
    position = [[0,0]] # start a x = y = 0
    for N in range(1, steps):
        previous_position_x = position[i-1][0]
        previous_position_y = position[i-1][1]

        new_position_x = random.choice(previous_position_x, previous_position_x + 1, previous_position_x - 1)
        new_position_y = random.choice(previous_position_y, previous_position_y + 1, previous_position_y - 1)

        position.append([new_position_x, new_position_y])
    return position


def create_single_particle_diffusion_with_momentum(steps):
