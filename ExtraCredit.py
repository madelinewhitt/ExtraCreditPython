# The program in this file is the individual work of Madeline Whitton

"""extracredit.py"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

if __name__ == "__main__":
    string = str(input())
    lst = string.split()
    num_prisms = int(lst[0])
    DegAcc = float(lst[1])
    
    prisms = []

    # Read in prisms and their dimensions
    for var in range(num_prisms):
        string = input()
        lst = string.split()
        prism = [float(num) for num in lst]        
        prisms.append(prism)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # isolate x y and z values into individual lists 
    x_values = [sublist[::3] for sublist in prisms]
    y_values = [sublist[1::3] for sublist in prisms]
    z_values = [sublist[2::3] for sublist in prisms]

    # 3-D Rectangular Bounding Box
    max_x = max(max(sublist) for sublist in x_values)
    min_x = min(min(sublist) for sublist in x_values)
    max_y = max(max(sublist) for sublist in y_values)
    min_y = min(min(sublist) for sublist in y_values)
    max_z = max(max(sublist) for sublist in z_values)
    min_z = min(min(sublist) for sublist in z_values)

    # Set the axes limits to make the bounding box larger
    padding = 0  # Adjust padding to your liking
    ax.set_xlim([min_x-padding, max_x+padding])
    ax.set_ylim([min_y-padding, max_y+padding])
    ax.set_zlim([min_z-padding, max_z+padding])

    for vertices in prisms:
        x1, y1, z1, x2, y2, z2 = vertices
        # Compute the other two vertices to form a rectangle in 3D
        vertices = [
            [x1, y1, z1], [x2, y1, z1], [x2, y2, z1], [x1, y2, z1],  # Bottom face
            [x1, y1, z2], [x2, y1, z2], [x2, y2, z2], [x1, y2, z2]   # Top face
        ]
        # Indices of vertices that form the rectangle sides
        sides = [
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[1], vertices[2], vertices[6], vertices[5]],
            [vertices[2], vertices[3], vertices[7], vertices[6]],
            [vertices[3], vertices[0], vertices[4], vertices[7]],
            [vertices[4], vertices[5], vertices[6], vertices[7]],
            [vertices[0], vertices[1], vertices[2], vertices[3]]
        ]
        poly3d = [sides[0], sides[1], sides[2], sides[3], sides[4], sides[5]]
        ax.add_collection3d(Poly3DCollection(poly3d, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.65))

    # Set labels and show plot
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.tight_layout()
    plt.show()
