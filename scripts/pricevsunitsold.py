import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/books_sales_and_ratings.csv")   

# Quick overview
print(df.head())
print(df.info())
print(df.describe())

# Scatter Plot – Price vs Units Sold
# Check if cheaper books sell more units:
plt.figure(figsize=(10,6))
plt.scatter(df['sale price'], df['units sold'], alpha=0.6, color='red')
plt.xlabel('Sale Price ($)')
plt.ylabel('Units Sold')
plt.title('Sale Price vs Units Sold')
plt.grid(True)
plt.show()
