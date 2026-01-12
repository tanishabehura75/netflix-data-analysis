import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")



# Quick data check
print(df.head())
print(df.shape)

# 1. Movies vs TV Shows
type_counts = df['type'].value_counts()

plt.figure()
type_counts.plot(kind='bar')
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("movies_vs_tv.png")
plt.show()

# 2. Top 10 Genres
genres = df['listed_in'].str.split(', ').explode()
top_genres = genres.value_counts().head(10)

plt.figure(figsize=(10, 5))
top_genres.plot(kind='bar')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("top_10_genres.png")
plt.show()
# 3. Content Growth Over the Years
year_counts = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(10, 5))
year_counts.plot(kind='line')
plt.title("Netflix Content Growth Over the Years")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("content_growth_by_year.png")
plt.show()
