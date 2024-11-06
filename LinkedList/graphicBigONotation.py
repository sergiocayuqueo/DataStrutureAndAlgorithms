import matplotlib.pyplot as plt
import numpy as np

# Create a figure to visualize different Big-O notations.
fig, ax = plt.subplots(figsize=(12, 8))

# Define a range for the x values to simulate input size (n).
x = np.linspace(1, 50, 400)

# Define Big-O functions
y_O1 = np.ones_like(x)  # O(1)
y_On = x  # O(n)
y_Ologn = np.log2(x)  # O(log n)
y_Onlogn = x * np.log2(x)  # O(n log n)
y_On2 = x**2  # O(n^2)
y_O2n = 2**x  # O(2^n)

# Plot each Big-O function with appropriate labels
ax.plot(x, y_O1, label='O(1)', color='blue')
ax.plot(x, y_Ologn, label='O(log n)', color='green')
ax.plot(x, y_On, label='O(n)', color='orange')
ax.plot(x, y_Onlogn, label='O(n log n)', color='purple')
ax.plot(x, y_On2, label='O(n^2)', color='red')
ax.plot(x, y_O2n, label='O(2^n)', color='brown')

# Set axis labels and title
ax.set_xlabel('Input Size (n)', fontsize=14)
ax.set_ylabel('Time Complexity', fontsize=14)
ax.set_title('Big-O Notation Visualized', fontsize=16)

# Set the legend for each Big-O notation
ax.legend()

# Limit y-axis to make visualization clearer
ax.set_ylim(0, 100)

# Display the plot
plt.grid(True)
plt.show()
































