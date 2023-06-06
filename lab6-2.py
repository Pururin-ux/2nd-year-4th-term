import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
a = 0.5
h = 0.1
tau = 0.001
N = int(1 / h) + 1
M = int(0.1 / tau) + 1

# Define the functions
def a_squared(x, t):
    return 0.5

def f(x, t):
    return 0

def mu1(t):
    return 1

def mu2(t):
    return 0.5

def phi(x):
    return np.sin(np.pi * x)

# Initialize the temperature array
U = np.zeros((N, M))

# Set the initial condition
U[:, 0] = phi(np.linspace(0, 1, N))

# Apply the boundary conditions
U[0, :] = mu1(np.linspace(0, 0.1, M))
U[-1, :] = mu2(np.linspace(0, 0.1, M))

# Solve the problem using the explicit difference scheme
for j in range(0, M-1):
    for i in range(1, N-1):
        U[i, j+1] = (1 - 2 * a_squared(i * h, j * tau) * tau / h**2) * U[i, j] + \
                    a_squared(i * h, j * tau) * tau / h**2 * (U[i-1, j] + U[i+1, j]) + \
                    tau * f(i * h, j * tau)

# Plot the temperature profile at the initial and final time
x = np.linspace(0, 1, N)
t_initial = 0
t_final = 0.1

plt.plot(x, U[:, 0], label='t = {}'.format(t_initial))
plt.plot(x, U[:, -1], label='t = {}'.format(t_final))
plt.xlabel('x')
plt.ylabel('Temperature')
plt.title('Temperature Profile')
plt.legend()
plt.grid(True)
plt.show()
