import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv("data/books_sales_and_ratings.csv")

# Ensure 'images' folder exists
if not os.path.exists("images"):
    os.makedirs("images")

# Columns we want in the heatmap
numeric_cols = ['Author_Rating', 'Book_average_rating', 'Book_ratings_count', 
                'gross sales', 'publisher revenue', 'sale price', 'sales rank', 'units sold']

# Convert all to numeric, coerce errors (non-numeric -> NaN)
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with NaN in these numeric columns
df_numeric = df[numeric_cols].dropna()

# Plot heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Between Numeric Features')
plt.tight_layout()
plt.savefig("images/correlation_heatmap.png", dpi=300)
plt.show()
