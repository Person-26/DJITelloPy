import math
import itertools
import numpy as np

def pathfinder(points):
    orders = itertools.permutations(points)
    lengths = np.zeros(len(orders))
    for i in range(len(orders)):
        lengths[i] += math.sqrt((points[i][0] + points[(i+1) % len(orders)][0]) ** 2 + (points[i][2] + points[(i+1) % len(orders)][2]) ** 2 + (points[i][2] + points[(i+1) % len(orders)][2]) ** 2)
    return orders[np.argmin(lengths) + 1]