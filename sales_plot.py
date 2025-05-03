import matplotlib.pyplot as plt

# Data for the products and their sales
products = ['A', 'B', 'C', 'D', 'E']
sales = [23, 75, 57, 90, 65]

# Create a bar plot
plt.figure(figsize=(8, 5))
plt.bar(products, sales, color='skyblue')

# Adding title and labels
plt.title('Sales of Products A to E')
plt.xlabel('Products')
plt.ylabel('Number of Sales')

# Show gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Ensure everything fits
plt.tight_layout()

# Save the plot as an image
plt.savefig('sales_plot.png')

# Display the plot
plt.show()
