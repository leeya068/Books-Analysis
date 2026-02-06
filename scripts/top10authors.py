import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/books_sales_and_ratings.csv")   

# Quick overview
print(df.head())
print(df.info())
print(df.describe())

# Top 10 Authors by Total Sales Revenue
top_authors = df.groupby('Author')['gross sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
top_authors.plot(kind='bar', color='green')
plt.xlabel('Author')
plt.ylabel('Total Gross Sales')
plt.title('Top 10 Authors by Gross Sales')
plt.xticks(rotation=45)
plt.show()
