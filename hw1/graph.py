import matplotlib.pyplot as plt

# Given data
iterations = range(10)  # Iterations from 0 to 9
average_returns = [
    295.7123108,
    2952.269043,
    523.1920776,
    5247.718262,
    5357.900879,
    4526.529785,
    4967.918457,
    5381.875488,
    5355.002441,
    5299.413086
]
std_devs = [
    300.240387,
    1722.418701,
    907.7667236,
    55.65332794,
    199.2852936,
    1177.380005,
    1344.844971,
    39.83282852,
    101.8049622,
    50.15550613

]

# Create a full-size figure
plt.figure(figsize=(8, 5))  # Set width and height in inches

# Create the plot with error bars
plt.errorbar(iterations, average_returns, yerr=std_devs, fmt='o-', capsize=5, capthick=2, label='Agent Average Return', color='black')

# Add horizontal lines for the expert mean and behavioral cloning mean
plt.axhline(y=5373.08, color='green', linestyle='--', linewidth=1.5, label='Expert Mean')
plt.axhline(y=295.71, color='red', linestyle='--', linewidth=1.5, label='BC Mean')

# Adding labels and title
plt.xlabel('Iterations')
plt.ylabel('Average Return')
plt.title('Average Return vs Iterations')

# Show all iterations on the x-axis
plt.xticks(iterations)

# Add light dotted horizontal lines for each y-tick
plt.grid(which='major', axis='y', linestyle=':', linewidth=0.75, alpha=0.8)

# Show legend in the bottom right corner
plt.legend(loc='lower right')

# Save the figure with high resolution
plt.savefig('full_size_graph_walker.png', bbox_inches='tight', dpi=300)

# Show the plot
plt.show()
