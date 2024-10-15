import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the sigmoid function
def sigmoid(x):
    return np.exp(x) / (1 + np.exp(x))

lob = -10.05
hib = 10.05

# Set up the figure, axis, and plot elements
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(lob, hib)
ax.set_ylim(-0.1, 1.1)
ax.set_xlabel('x')
ax.set_ylabel('σ(x)')
ax.set_title('Sigmoid Function Animation')

# Plot the sigmoid curve
x_values = np.linspace(lob, hib, 400)
y_values = sigmoid(x_values)
ax.plot(x_values, y_values, color='black', label='Sigmoid Curve')

# Plot the horizontal line for x value movement
ax.hlines(0, lob, hib, color='gray', linestyle='--', linewidth=1, label='x Line')

# Initialize points for x value and σ(x) value
x_circle, = ax.plot([], [], 'ro', label='x Value', markersize=10)  # Red circle for x value, markersize=10
y_circle, = ax.plot([], [], 'bo', label='σ(x) Value', markersize=10)  # Blue circle for σ(x) value, markersize=10

# Display the value at the top
value_text = ax.text(0.05, 0.95, '', transform=ax.transAxes, ha='left', va='top', fontweight='bold')

# Initialization function for the animation
def init():
    x_circle.set_data([], [])
    y_circle.set_data([], [])
    value_text.set_text('')
    return x_circle, y_circle, value_text

# Animation function: update the red and blue circles for each frame
def update(frame):
    x = frame
    y = sigmoid(x)
    
    # Update the position of the circles
    x_circle.set_data([x], [0])
    y_circle.set_data([x], [y])
    
    # Update the displayed text with the current x and σ(x) values in bold
    value_text.set_text(f'\n\n\n\n\n\nx = {x:.5f}, σ(x) = {y:.5f}')
    
    return x_circle, y_circle, value_text

# Set up the frames for the animation (x values from -10 to 10 in 0.05 intervals)
# Add additional frames for a pause effect at lob and 0
frames = []

# Pause at lob
frames.extend([lob] * 20)

# Values from lob to 0
frames.extend(np.arange(lob, 0, 0.05))

# Pause at 0
frames.extend([0] * 20)

# Values from 0 to hib
frames.extend(np.arange(0, hib, 0.05))

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=50, repeat=False)

# Show the legend
ax.legend()

# Display the animation
plt.show()
