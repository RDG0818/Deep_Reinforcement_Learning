import matplotlib.pyplot as plt

# Example data for 4 different lines: Replace these with your actual data
env_steps = [i for i in range(100)]

# Data for 4 different experiments or models
average_returns_1 = [30.0, 44.55555725, 42.0, 69.16666412, 77.0, 79.16666412, 80.40000153, 57.2857132, 69.5, 109.8000031, 87.0, 115.25, 139.0, 96.40000153, 149.3333282, 143.6666718, 184.3333282, 127.0, 183.3333282, 154.3333282, 129.5, 110.25, 145.6666718, 143.0, 200.0, 200.0, 200.0, 200.0, 190.6666718, 200.0, 167.6666718, 176.0, 160.0, 154.0, 200.0, 182.6666718, 156.6666718, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 174.6666718, 200.0, 200.0, 200.0, 200.0, 188.3333282, 200.0, 169.3333282, 168.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 121.5, 74.0, 109.8000031, 106.1999969, 169.6666718, 141.75, 187.0, 200.0, 194.0, 195.3333282, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0]
average_returns_2 = [43.5, 41.59999847, 51.88888931, 73.16666412, 86.80000305, 75.33333588, 86.19999695, 105.5, 112.5, 155.6666718, 189.3333282, 150.3333282, 197.0, 182.3333282, 197.3333282, 167.6666718, 194.3333282, 200.0, 200.0, 200.0, 173.3333282, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 177.6666718, 139.6666718, 140.0, 200.0, 200.0, 191.6666718, 200.0, 200.0, 165.3333282, 200.0, 182.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 195.6666718, 200.0, 194.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0]
average_returns_3 = [31.1428566, 29.9285717, 53.0, 84.40000153, 64.14286041, 81.59999847, 83.80000305, 119.25, 133.3333282, 140.6666718, 162.6666718, 158.3333282, 154.6666718, 195.0, 200.0, 200.0, 198.3333282, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0]
average_returns_4 = [28.13333321, 41.79999924, 52.5, 55.25, 80.40000153, 99.80000305, 108.1999969, 85.80000305, 89.40000153, 117.75, 143.0, 178.0, 200.0, 141.3333282, 185.0, 184.3333282, 176.0, 188.6666718, 175.0, 165.6666718, 181.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 192.6666718, 200.0, 200.0, 200.0, 197.6666718, 200.0, 200.0, 200.0, 195.0, 200.0, 199.6666718, 190.6666718, 198.3333282, 200.0, 200.0, 193.3333282, 184.3333282, 189.0, 200.0, 196.6666718, 188.6666718, 197.6666718, 198.6666718, 200.0, 200.0, 197.3333282, 200.0, 200.0, 200.0, 191.0, 193.6666718, 181.6666718, 200.0, 185.6666718, 188.3333282, 178.0, 185.3333282, 200.0, 196.6666718, 187.6666718, 200.0, 171.0, 191.0, 170.0, 200.0, 197.3333282, 197.0, 200.0, 200.0, 200.0, 198.0, 200.0, 200.0, 200.0, 200.0, 190.3333282, 197.3333282, 190.0, 200.0, 187.6666718, 168.0, 194.0, 185.3333282]

import numpy as np

# Function to apply a simple moving average
def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Example of using a window size of 5 for smoothing
window_size = 5
smoothed_returns_1 = moving_average(average_returns_1, window_size)
smoothed_returns_2 = moving_average(average_returns_2, window_size)
smoothed_returns_3 = moving_average(average_returns_3, window_size)
smoothed_returns_4 = moving_average(average_returns_4, window_size)

# Adjust the environment steps to match the size of the smoothed data
smoothed_env_steps = env_steps[:len(smoothed_returns_1)]  # Adjust length accordingly

# Plot the smoothed data
plt.figure(figsize=(10, 6))

# Plot with smoothed data
plt.plot(smoothed_env_steps, smoothed_returns_1, label='Vanilla Policy Gradients (smoothed)', color='b', linestyle='-')
plt.plot(smoothed_env_steps, smoothed_returns_2, label='Reward To Go (smoothed)', color='r', linestyle='-')
plt.plot(smoothed_env_steps, smoothed_returns_3, label='Normalized Advantages (smoothed)', color='g', linestyle='-')
plt.plot(smoothed_env_steps, smoothed_returns_4, label='Reward To Go and Normalized Advantages (smoothed)', color='orange', linestyle='-')

# Adding title and labels with increased font size for clarity
plt.title('Smoothed Average Returns vs. Environment Steps (Cartpole, Large Batches)', fontsize=16)
plt.xlabel('Environment Steps', fontsize=14)
plt.ylabel('Average Return (Smoothed)', fontsize=14)

# Adding legend with larger font size
plt.legend(fontsize=12)

# Enhancing grid with lighter lines
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.tight_layout()
plt.show()
