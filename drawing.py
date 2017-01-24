import matplotlib.pyplot as plt
import numpy as np
import time



def create_Fig(initial_image):
    size = np.shape(initial_image)

    # create the figure
    fig = plt.figure()

    #create the axis object:
    ax = fig.add_subplot(111)

    # draw the initial image as a heat map without interpolation
    im = ax.imshow(initial_image, interpolation="none", cmap='gnuplot2')

    # Fixing the grid:
    # major ticks every 20, minor ticks every 5
    x_ticks = np.arange(-0.5, size[1]+.5,1)
    y_ticks = np.arange(-0.5, size[0]+.5,1)

    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)

    # and a corresponding grid
    ax.grid(which='both')

    # Turn off tick labels
    ax.set_yticklabels([])
    ax.set_xticklabels([])

    # Show the initial image
    plt.show(block=False)

    print "please press enter to proceed ..."
    raw_input()
    return fig, im

def draw_State(fig, im, current_image, delay):
    # wait for a given time if needed.
    if delay != 0:
        time.sleep(delay)

    # replace the image contents
    im.set_array(current_image)

    # redraw the figure
    fig.canvas.draw()

    print "please press enter to proceed ..."
    raw_input()


if __name__ == "__main__":

    #N=2
    #M=2
    #image1 = np.random.randint(2, size=(N,M))
    image1=[[0,0,0,0],[1000,1000,1000,1000]]
    f,i = create_Fig(image1)

    #image2 = np.random.randint(2, size=(N,M))
    #draw_State(f, i, image1, 6)
