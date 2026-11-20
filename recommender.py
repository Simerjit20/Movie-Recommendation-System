import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load movie dataset
movies = pd.read_csv("dataset/movies.csv")


# Fill missing genres
movies["genres"] = movies["genres"].fillna("")


# Convert genres into numerical vectors
cv = CountVectorizer(tokenizer=lambda x: x.split("|"), token_pattern=None)

genre_matrix = cv.fit_transform(movies["genres"])


# Calculate similarity between movies
similarity = cosine_similarity(genre_matrix)


# Recommendation function
def recommend_movies(movie_name):

    movie_name = movie_name.lower()

    matching_movies = movies[
        movies["title"].str.lower() == movie_name
    ]

    if matching_movies.empty:
        return None

    movie_index = matching_movies.index[0]

    similarity_scores = list(enumerate(similarity[movie_index]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similar_movies = similarity_scores[1:6]

    recommendations = []

    for index, score in similar_movies:
        recommendations.append(movies.iloc[index]["title"])

    return recommendations