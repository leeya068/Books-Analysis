import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/books_sales_and_ratings.csv")   

# Quick overview
print(df.head())
print(df.info())
print(df.describe())

# Average Book Ratings by Genre
avg_ratings = df.groupby('genre')['Book_average_rating'].mean().sort_values(ascending=False)

plt.figure(figsize=(12,6))
avg_ratings.plot(kind='bar', color='purple')
plt.xlabel('Genre')
plt.ylabel('Average Book Rating')
plt.title('Average Book Ratings by Genre')
plt.xticks(rotation=45)
plt.show()
