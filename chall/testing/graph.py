import matplotlib.pyplot as plt
import numpy as np

# Define the range for x
x = np.linspace(-5, 5, 400)
# Define the absolute value function
y = np.abs(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$y = |x|$', color='b')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# Set the x and y axis labels
plt.xlabel('x')
plt.ylabel('y')

# Set the title
plt.title('Graph of y = |x|')

# Add a legend
plt.legend()

# Show the plot
plt.show()
