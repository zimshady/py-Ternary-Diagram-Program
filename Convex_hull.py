import numpy as np
from scipy.spatial import ConvexHull

def make_conv_hull(data):
    points = data
    points = np.array(points)
    hull = ConvexHull(points)
    cent = np.mean(points)
    pts = []

    return hull.simplices
