import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/books_sales_and_ratings.csv")   # forward slash


# Quick overview
print(df.head())
print(df.info())
print(df.describe())

# Distribution of Publishing Years
# See which years produced the most books
plt.figure(figsize=(12,6))
df['Publishing Year'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.xlabel('Publishing Year')
plt.ylabel('Number of Books')
plt.title('Number of Books Published Each Year')
plt.xticks(rotation=45)
plt.show()
