import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/books_sales_and_ratings.csv")   

# Quick overview
print(df.head())
print(df.info())
print(df.describe())

# Top Genres by Total Units Sold
genre_sales = df.groupby('genre')['units sold'].sum().sort_values(ascending=False)

plt.figure(figsize=(12,6))
genre_sales.plot(kind='bar', color='teal')
plt.xlabel('Genre')
plt.ylabel('Total Units Sold')
plt.title('Top Genres by Units Sold')
plt.xticks(rotation=45)
plt.show()
