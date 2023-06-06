import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the ODE
def ode_func(y, x, a, b):
    return [y[1], (1 + np.cos(x)) / np.sqrt(a**2 + x**2) * y[0] -
            x / (b + x**2) * y[1] + np.exp(-a * x**2)]

# Define the boundary conditions
beta1 = -0.5
alfa2 = 4.50
beta2 = 0.3

# Define the wrapper function for the ODE with additional arguments
def ode_wrapper(y, x):
    return ode_func(y, x, 0.87, 0.78)

# Define the wrapper function for the boundary conditions with additional arguments
def bc_wrapper(ya_yb, x):
    return bc_func(ya_yb, x, beta1, alfa2, beta2)

# Define the derivative function for the boundary conditions
def bc_func(ya_yb, x, beta1, alfa2, beta2):
    ya, yb = ya_yb[0], ya_yb[1]
    return [ya + beta1 * yb - 1, alfa2 * yb + beta2 * yb - 4.7]

# Set up the grid
x = np.linspace(0, 1, 100)

# Solve the ODE
y = odeint(ode_wrapper, [0, 0], x, tcrit=[0, 1], h0=1e-8)

# Extract the solution
y_solution = y[:, 0]

# Plot the solution
plt.plot(x, y_solution)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of the ODE')
plt.grid(True)
plt.show()
