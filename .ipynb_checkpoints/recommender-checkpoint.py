import pandas as pd 

ratings_path = "ml-32m/ratings.csv"
movies_path = "ml-32m/movies.csv"

ratings_df_32m = pd.read_csv(ratings_path)
movies_df_32m = pd.read_csv(movies_path)

print("Ratings Data (32M):")
print(ratings_df_32m.head())

print("Movies Data (32M):")
print(movies_df_32m.head())

# Merge
ratings_df_32m = pd.merge(ratings_df_32m, movies_df_32m[['movieId', 'title']], on='movieId', how='inner')
print(ratings_df_32m.head())