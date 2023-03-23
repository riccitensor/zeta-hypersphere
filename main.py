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
    
# Example usage:
s = 2  # You can use any complex number as input
point_on_4d_sphere = zeta_to_4d_sphere(s)
print(point_on_4d_sphere)

# Create a list of complex numbers to use as input for zeta_to_4d_sphere
complex_numbers = [complex(i, j) for i in np.linspace(0, 10, 100) for j in np.linspace(0, 10, 100)]

# Plot the 4D hypersphere generated using zeta_to_4d_sphere
plot_4d_sphere_from_zeta(complex_numbers)
