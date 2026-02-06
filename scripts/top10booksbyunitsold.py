import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/books_sales_and_ratings.csv")   # forward slash

# Quick overview
print(df.head())
print(df.info())
print(df.describe())

top_books = df.sort_values(by='units sold', ascending=False).head(10)

plt.figure(figsize=(12,6))
plt.barh(top_books['Book Name'], top_books['units sold'], color='orange')
plt.xlabel('Units Sold')
plt.ylabel('Book Name')
plt.title('Top 10 Books by Units Sold')
plt.gca().invert_yaxis()  # Highest units sold on top
plt.show()
