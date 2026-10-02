# Movie Recommendation System

## Project Overview

This project implements a content-based Movie Recommendation System using the TMDB 5000 movie dataset.

The system recommends movies that are similar to a selected movie by analyzing movie metadata such as:

- Movie overview
- Genres
- Keywords
- Cast
- Director

TF-IDF is used to convert the movie metadata into numerical features, and cosine similarity is used to find similar movies.

## Dataset

The project uses the following TMDB datasets:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

The two datasets are merged using the movie ID.

## Project Workflow

1. Load the TMDB datasets
2. Perform Exploratory Data Analysis
3. Handle missing values
4. Merge movie and credits data
5. Clean genres and keywords
6. Extract the top cast members
7. Extract the director
8. Create a combined `tags` feature
9. Apply TF-IDF vectorization
10. Calculate cosine similarity
11. Build the movie recommendation function
12. Perform qualitative evaluation
13. Save the trained TF-IDF vectorizer and cleaned movie data
14. Create a reusable recommendation script

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

## Recommendation Method

### TF-IDF

TF-IDF converts the combined movie metadata into numerical feature vectors.

### Cosine Similarity

Cosine similarity measures the similarity between movie feature vectors.

Movies with more similar metadata receive higher similarity scores and are recommended to the user.

## Sample Results

The recommendation system was tested with sample movies including:

- Avatar
- Interstellar
- The Dark Knight Rises

For example, when `Interstellar` is entered, the system recommends movies such as:

- Moonraker
- Silent Running
- 2001: A Space Odyssey
- Lost in Space
- Cargo
- Armageddon
- Planet of the Apes
- Gravity
- Space Pirate Captain Harlock
- Mission to Mars

## Project Structure

```text
Project-1_Movie-Recommendation-System
│
├── data
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── models
│   └── tfidf_vectorizer.pkl
│
├── notebooks
│   └── movie_recommendation.ipynb
│
├── outputs
│   └── cleaned_movies.csv
│
├── src
│   └── recommender.py
│
├── README.md
└── requirements.txt
```

## How to Run

### 1. Install the required packages

```bash
pip install -r requirements.txt
```

### 2. Run the recommendation script

From the project folder, run:

```bash
py -3.14 src/recommender.py
```

### 3. Enter a movie name

The program will ask:

```text
Enter a movie name:
```

Enter a movie available in the dataset, for example:

```text
Interstellar
```

The system will then display the recommended movies along with their similarity scores.

## Qualitative Evaluation

The system was evaluated using sample movie queries.

The recommendations showed that movies with similar genres, keywords, cast, director, and overview information were generally grouped together.

For example, querying `The Dark Knight Rises` produced recommendations including other Batman-related movies such as `The Dark Knight` and `Batman Begins`.

## Conclusion

The project demonstrates a content-based movie recommendation approach using movie metadata.

By combining metadata cleaning, TF-IDF feature extraction, and cosine similarity, the system can recommend movies similar to a movie selected by the user.