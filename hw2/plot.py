import matplotlib.pyplot as plt

# Example data for 4 different lines: Replace these with your actual data
env_steps = [i for i in range(100)]

# Data for 4 different experiments or models
average_returns_1 = [31.38461494, 44.0, 55.125, 36.38461685, 42.20000076, 73.66666412, 60.0, 60.2857132, 65.7142868, 50.25, 60.57143021, 79.5, 84.59999847, 81.59999847, 95.19999695, 92.0, 75.0, 83.16666412, 96.19999695, 100.0, 95.40000153, 89.80000305, 116.5, 123.0, 114.5, 151.0, 158.6666718, 200.0, 184.6666718, 147.0, 200.0, 146.0, 151.0, 200.0, 169.0, 142.6666718, 133.6666718, 158.6666718, 131.5, 190.0, 200.0, 185.0, 175.3333282, 192.6666718, 200.0, 115.25, 152.6666718, 116.75, 137.6666718, 141.6666718, 161.6666718, 177.3333282, 150.3333282, 200.0, 168.6666718, 151.6666718, 200.0, 200.0, 160.6666718, 166.0, 172.3333282, 166.6666718, 165.0, 159.0, 159.0, 158.3333282, 181.0, 200.0, 200.0, 188.3333282, 182.0, 153.3333282, 135.3333282, 134.5, 139.5, 137.3333282, 142.6666718, 147.0, 153.3333282, 127.25, 125.75, 124.25, 119.75, 119.75, 123.0, 124.75, 120.25, 118.5, 118.75, 104.25, 115.25, 95.40000153, 72.66666412, 71.83333588, 59.57143021, 57.8571434, 53.375, 48.11111069, 48.55555725, 46.0]  # Line 1
average_returns_2 = [32.53845978, 33.53845978, 63.0, 89.16666412, 68.14286041, 84.19999695, 110.5, 102.8000031, 112.0, 151.0, 149.6666718, 163.0, 155.6666718, 152.6666718, 200.0, 159.0, 200.0, 174.3333282, 186.3333282, 200.0, 175.3333282, 172.3333282, 154.0, 135.3333282, 125.0, 126.0, 133.75, 147.3333282, 135.3333282, 131.75, 133.6666718, 137.6666718, 158.6666718, 173.3333282, 200.0, 200.0, 176.6666718, 200.0, 200.0, 162.0, 186.3333282, 184.6666718, 154.0, 131.25, 144.0, 154.0, 156.3333282, 192.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 199.0, 171.3333282, 151.6666718, 171.6666718, 175.0, 192.6666718, 196.6666718, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 135.0, 171.6666718]  # Line 2
average_returns_3 = [35.08333206, 42.29999924, 42.0, 45.22222137, 42.20000076, 70.66666412, 72.66666412, 75.0, 88.80000305, 71.16666412, 77.0, 58.8571434, 62.7142868, 104.25, 88.80000305, 106.5, 129.25, 105.5, 83.59999847, 84.59999847, 81.66666412, 85.19999695, 75.5, 74.66666412, 108.75, 98.0, 73.83333588, 102.0, 93.59999847, 118.4000015, 158.6666718, 133.25, 164.0, 167.6666718, 200.0, 200.0, 199.6666718, 200.0, 200.0, 196.6666718, 200.0, 200.0, 200.0, 200.0, 173.6666718, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0]   # Line 3
average_returns_4 = [34.5, 34.66666794, 39.27272797, 44.66666794, 87.0, 81.80000305, 102.25, 73.5, 72.33333588, 92.59999847, 101.0, 110.25, 177.6666718, 86.80000305, 153.3333282, 176.6666718, 200.0, 200.0, 195.6666718, 191.0, 200.0, 159.0, 143.3333282, 136.0, 168.6666718, 164.0, 200.0, 180.3333282, 200.0, 200.0, 198.3333282, 182.3333282, 200.0, 200.0, 161.3333282, 168.3333282, 186.3333282, 200.0, 191.3333282, 199.6666718, 200.0, 200.0, 194.0, 200.0, 200.0, 200.0, 167.3333282, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 140.25, 190.6666718, 183.3333282, 189.6666718, 198.3333282, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 157.3333282, 147.0, 127.25, 100.0, 86.19999695, 101.75, 93.19999695, 97.0, 102.0, 112.5, 118.5, 113.0, 125.5, 141.3333282, 140.6666718, 149.3333282, 176.6666718, 195.6666718, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0]  # Line 4

import numpy as np

# Function to apply a simple moving average
def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Example of using a window size of 5 for smoothing
window_size = 7
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
plt.title('Smoothed Average Returns vs. Environment Steps (Cartpole)', fontsize=16)
plt.xlabel('Environment Steps', fontsize=14)
plt.ylabel('Average Return (Smoothed)', fontsize=14)

# Adding legend with larger font size
plt.legend(fontsize=12)

# Enhancing grid with lighter lines
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.tight_layout()
plt.show()
