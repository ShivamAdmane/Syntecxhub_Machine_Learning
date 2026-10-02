import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity


# Load saved files
movies = pd.read_csv("outputs/cleaned_movies.csv")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")


# Create TF-IDF matrix from saved movie tags
tfidf_matrix = tfidf.transform(movies["tags"])


def recommend_movies(movie_title, num_recommendations=10):
    movie_title = movie_title.lower()

    matches = movies[
        movies["title"].str.lower() == movie_title
    ]

    if matches.empty:
        print("Movie not found in the dataset.")
        return

    movie_index = matches.index[0]

    similarity_scores = cosine_similarity(
        tfidf_matrix[movie_index],
        tfidf_matrix
    ).flatten()

    similar_movies = similarity_scores.argsort()[::-1]

    print(f"\nRecommendations for: {movies.iloc[movie_index]['title']}\n")

    count = 0

    for index in similar_movies:
        if index == movie_index:
            continue

        print(
            f"{movies.iloc[index]['title']} "
            f"(similarity: {similarity_scores[index]:.3f})"
        )

        count += 1

        if count == num_recommendations:
            break


if __name__ == "__main__":
    movie_name = input("Enter a movie name: ")
    recommend_movies(movie_name)