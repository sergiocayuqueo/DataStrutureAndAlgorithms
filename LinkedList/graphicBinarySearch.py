import matplotlib.pyplot as plt
import numpy as np

# Visualizing Binary Search algorithm with Python
# This will simulate binary search on a sorted array and show the steps

# Function to perform binary search on a sorted list and visualize each step


# Enhancing visualization to clearly show the halving of the array

def binary_search_visualization_enhanced(arr, target):
    left, right = 0, len(arr) - 1
    step = 1  # Track steps for demonstration

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.grid(True)

    while left <= right:
        ax.clear()  # Clear previous plot for each step
        mid = (left + right) // 2  # Middle index

        # Plot the entire array with a color gradient
        colors = ['grey'] * len(arr)  # Default color for all elements
        # Highlight the current search range
        colors[left:right + 1] = ['skyblue'] * (right - left + 1)
        colors[mid] = 'red'  # Highlight middle element in red

        # Plot the array with color coding for clarity
        ax.bar(range(len(arr)), arr, color=colors, edgecolor='black')

        # Display current bounds and mid element in plot title
        ax.set_title(
            f"Step {step}: Left={left}, Mid={mid}, Right={right}", fontsize=14)
        ax.set_xticks(range(len(arr)))  # Show each index for reference
        ax.set_yticks(arr)

        # Check if the middle element is the target
        if arr[mid] == target:
            ax.bar(mid, arr[mid], color='green',
                   edgecolor='black', label="Target Found")
            ax.legend()
            plt.pause(2.0)  # Pause to highlight the found element
            break
        elif arr[mid] < target:
            left = mid + 1  # Discard left half
        else:
            right = mid - 1  # Discard right half

        plt.pause(5.5)  # Pause to show each step
        step += 1

    # Display final outcome if target is not found
    if left > right:
        ax.set_title(f"Target {target} Not Found", fontsize=16)


sorted_array = list(range(0, 21))
print(sorted_array)
target_element = 19

# Run the enhanced visualization for binary search
binary_search_visualization_enhanced(sorted_array, target_element)
