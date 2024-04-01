import pandas as pd
import matplotlib.pyplot as plt

# Access data from Power BI dataset
data = dataset[['Category of Departments', 'Males_needed', 'Females_needed']]

# Define colors for bars
color_males = '#1F243B'
color_females = '#E66C37'

# Create a bar plot
plt.figure(figsize=(10, 6))
bars1 = plt.bar(range(len(data)), data['Males_needed'], color=color_males, label='Males Needed')
bars2 = plt.bar(range(len(data)), data['Females_needed'], bottom=data['Males_needed'], color=color_females, label='Females Needed')
plt.xlabel('Departments', fontsize=12, fontweight='bold')  # Increase font size and make department names bold
plt.ylabel('Number of Individuals Needed', fontsize=12, fontweight='bold')  # Increase font size and make y-axis label bold
plt.title('Additional Males and Females Needed', fontsize=14, fontweight='bold')  # Increase font size and make title bold
plt.xticks(range(len(data)), data['Category of Departments'], rotation=45, ha='right')  # Rotate department names
plt.yticks(fontsize=10)  # Increase font size of y-axis ticks
plt.grid(axis='y', linestyle='--', alpha=0.5)  # Add horizontal grid lines
plt.legend(fontsize=10)  # Increase font size of legend

# Annotate the bars with their values
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height / 2, str(int(height)), ha='center', va='center', fontsize=10, color='white', fontweight='bold')

# Add a border around bars
for spine in plt.gca().spines.values():
    spine.set_visible(True)
    spine.set_color('black')

# Show plot
plt.tight_layout()
plt.show()