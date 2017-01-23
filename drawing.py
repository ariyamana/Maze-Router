import matplotlib.pyplot as plt
import numpy as np
import time

def create_Fig(initial_image):
    # create the figure
    fig = plt.figure()

    #create the axis object:
    ax = fig.add_subplot(111)

    # draw the initial image as a heat map without interpolation
    im = ax.imshow(initial_image, interpolation="none" )

    # Show the initial image
    plt.show(block=False)

    return fig, im


def draw_State(fig, im, current_image, delay):

    # wait for a given time if needed.
    if delay != 0:
        time.sleep(delay)

    # replace the image contents
    im.set_array(current_image)

    # redraw the figure
    fig.canvas.draw()

if __name__ == "__main__":
    
    N=10
    M=4
    image1 = np.random.randint(2, size=(N,M))
    f,i = create_Fig(image1)

    image2 = np.random.randint(2, size=(N,M))
    draw_State(f, i, image2, 6)
