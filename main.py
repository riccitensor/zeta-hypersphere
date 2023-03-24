import mpmath
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def zeta_to_4d_sphere(s):
    zeta_value = mpmath.zeta(s)
    real_part = float(zeta_value.real)
    imag_part = float(zeta_value.imag)

    # Map the real and imaginary parts to the range [0, 2 * pi]
    theta1 = (real_part % (2 * np.pi))
    theta2 = (imag_part % (2 * np.pi))

    # Convert the angles to Cartesian coordinates on a 4D sphere with radius 1
    x = np.cos(theta1) * np.sin(theta2)
    y = np.sin(theta1) * np.sin(theta2)
    z = np.cos(theta1) * np.cos(theta2)
    w = np.sin(theta1) * np.cos(theta2)

    return x, y, z, w

def stereographic_projection(x, y, z, w):
    # Stereographic projection from 4D to 3D
    return x / (1 - w), y / (1 - w), z / (1 - w)

def plot_4d_sphere_from_zeta(complex_numbers):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    for s in complex_numbers:
        x, y, z, w = zeta_to_4d_sphere(s)
        x3, y3, z3 = stereographic_projection(x, y, z, w)

        ax.scatter(x3, y3, z3, c="b", marker="o", s=10)

    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")

    plt.show()
    
def plot_4d_sphere_multiple_projections(complex_numbers):
    data = np.array([zeta_to_4d_sphere(s) for s in complex_numbers])

    fig, axs = plt.subplots(1, 3, figsize=(18, 6))

    # Prepare a colormap and a normalization function for color mapping
    cmap = cm.get_cmap("viridis")
    norm = plt.Normalize(-1, 1)

    for i, (x_idx, y_idx) in enumerate([(0, 1), (0, 2), (1, 2)]):
        for point in data:
            x, y = point[x_idx], point[y_idx]
            w = point[3]

            color = cmap(norm(w))
            size = 10 + 40 * ((w + 1) / 2)

            axs[i].scatter(x, y, c=color, marker="o", s=size, alpha=0.7)

        axs[i].set_xlabel(f"Axis {x_idx}")
        axs[i].set_ylabel(f"Axis {y_idx}")

    plt.show()
    
    
# Example usage:
s = 2  # You can use any complex number as input
point_on_4d_sphere = zeta_to_4d_sphere(s)
print(point_on_4d_sphere)

# Create a list of complex numbers to use as input for zeta_to_4d_sphere
complex_numbers = [complex(i, j) for i in np.linspace(0, 10, 100) for j in np.linspace(0, 10, 100)]

# Plot the 4D hypersphere generated using zeta_to_4d_sphere
plot_4d_sphere_from_zeta(complex_numbers)

# Plot the 2D projections
plot_4d_sphere_multiple_projections(complex_numbers)
