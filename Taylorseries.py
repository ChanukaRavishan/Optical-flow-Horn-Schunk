
import cv2
import numpy as np
from matplotlib import pyplot as plt
#to apply gausian laplace to n dimensional array
from scipy.ndimage import convolve
import os
from argparse import ArgumentParser

"""
see readme for running instructions
"""


def show_image(name, image):
    if image is None:
        return

    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



#computing magnitude in each 8 pixels. return magnitude average
#input: u,v vectors
#output: magnitude average
#calculates magnitude average of the flow vectors

def get_magnitude(u, v):
    # scaling factor - determines the sensitivity of flow vectors to motion
    scale = 3
    sum = 0.0
    counter = 0.0

    #process every 8th element, reducing the total number of flow vectors considering efficiency
    for i in range(0, u.shape[0], 8):
        for j in range(0, u.shape[1],8):
            counter += 1
            dy = v[i,j] * scale
            dx = u[i,j] * scale
            # Euclidean distance formula - magnitude of flow vector at the current position
            magnitude = (dx**2 + dy**2)**0.5
            sum += magnitude

    mag_avg = sum / counter

    return mag_avg
