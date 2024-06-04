import matplotlib.pyplot as plt
import random

# Define the colors and corresponding children counts
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']
children_counts = [random.randint(5, 20) for _ in colors]
bar_colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#9370DB']

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(colors, children_counts, color=bar_colors)

# Add title and labels
plt.title('Favorite Colors Among Children')
plt.xlabel('Color')
plt.ylabel('Number of Children')

# Show the bar chart
plt.show()
