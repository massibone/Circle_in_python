import matplotlib.pyplot as plt
import numpy as np

# Completing the square to convert the equation to standard form
h = 10
k = -3
r = np.sqrt(144)

# Setting up the range of x and y values
x_range = np.arange(h-r, h+r+0.1, 0.1)
y_range = k + np.sqrt(r**2 - (x_range - h)**2)
y_range_neg = k - np.sqrt(r**2 - (x_range - h)**2)

# Defining the function for the circle equation
def circle_eqn(x, h, k, r):
    return np.sqrt(r**2 - (x - h)**2) + k, -np.sqrt(r**2 - (x - h)**2) + k

# Plotting the circle with center and radius identified
plt.plot(x_range, circle_eqn(x_range, h, k, r)[0], color='blue')
plt.plot(x_range, circle_eqn(x_range, h, k, r)[1], color='blue')
plt.plot(h, k, marker='o', markersize=5, color='red')
plt.annotate("(" + str(h) + "," + str(k) + ")", xy=(h, k), xytext=(h + 1, k + 1))
plt.annotate("r = " + str(r), xy=(h, k), xytext=(h + 1, k + 5))
plt.xlabel("x")
plt.ylabel("y")
plt.title("Circle with center (" + str(h) + "," + str(k) + ") and radius " + str(r))
plt.show()