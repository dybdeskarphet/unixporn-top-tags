import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np

# Function to generate darker colors
def get_colors(num_colors):
    return [
        (
            np.random.uniform(0.3, 0.9),
            np.random.uniform(0.3, 0.9),
            np.random.uniform(0.3, 0.9),
        )
        for _ in range(num_colors)
    ]


# Load data
data = pd.read_csv("tag_counts.csv")
df = pd.DataFrame(data).head(30)

# Convert counts to percentages
total_count = df["Count"].sum()
df["Percentage"] = (df["Count"] / total_count) * 100

# Data for plotting
X = list(df.iloc[:, 0])[::-1]
Y = list(df.iloc[:, 2])[::-1]  # Use the percentage column

# Create figure and axes objects
fig, ax = plt.subplots(figsize=(15, 20))

# Generate darker colors
colors = get_colors(len(X))

# Create horizontal bar plot with different colors and increased bar thickness
bar_thickness = 0.9  # Adjust the thickness as needed
y_positions = range(len(X))
x_positions = range(len(Y))
bars = ax.barh(y_positions, Y, color=colors, height=bar_thickness)

# Set y-axis ticks and labels with increased font size
ax.set_yticks(y_positions)
ax.set_yticklabels(X, fontsize=14)  # Correctly setting the y-axis labels

# Manually set and format x-ticks
xticks = range(0, int(max(Y)) + 1, 2)  # Generate x-tick values
ax.set_xticks(xticks)  # Set the x-ticks
ax.set_xticklabels(
    [f"{x}%" for x in xticks], fontsize=14, rotation="vertical"
)  # Format and set x-tick labels


ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))  # Show only integer x-ticks
ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# Annotate bars with percentage values
# Annotate bars with percentage values
for bar in bars:
    width = bar.get_width()
    label_x_pos = width  # Adjust this value as needed to position the label closer to the end of the bar
    ax.text(
        label_x_pos,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.2f}%",
        va="center",
        fontsize=10,
    )


ax.set_title("Tag Popularity in Unixporn Subreddit (Percentage)")
ax.set_xlabel("Percentage", fontsize=20)
ax.set_ylabel("Tags", fontsize=20)

# Show the plot
plt.savefig("graph.png", dpi=200)
plt.show()
