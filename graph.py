import matplotlib.animation as ani
import numpy as np
import matplotlib.pyplot as plt
import random

def create_and_animate_graph():
    color = 'red'
    fig = plt.figure()

    #plt.xticks(rotation=45, ha="right", rotation_mode="anchor") #rotate the x-axis values
    plt.ylabel('y')
    plt.xlabel('x')
    plt.legend(df1.columns)
    p = plt.plot(df1[:i].index, df1[:i].values)
    for i in range(0,4):
        p[i].set_color(color[i]) #set the colour of each curveimport matplotlib.animation as ani
    animator = ani.FuncAnimation(fig, buildmebarchart, interval = 100)
    plt.show()
