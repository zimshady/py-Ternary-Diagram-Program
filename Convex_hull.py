import numpy as np
from scipy.spatial import ConvexHull

def get_hull_vertices(data):
    points = data
    points = map(list, points)
    points = np.array(points)
    hull = ConvexHull(points)
    cent = np.mean(points)
    pts = []
    vert1 = points[hull.vertices[0],0]
    vert2 = points[hull.vertices[0],1]
    vert3 = points[hull.vertices[0],2]

    return vert1, vert2, vert3