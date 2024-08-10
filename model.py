import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

data = pd.read_csv('imdb_top_1000.csv')
data.columns = data.columns.str.strip()


def convert_runtime(runtime_str):
    try:
        if pd.isnull(runtime_str):
            return None
        runtime = ''.join(filter(str.isdigit, runtime_str))
        return int(runtime) if runtime else None
    except ValueError:
        return None

data['Runtime'] = data['Runtime'].apply(convert_runtime)

data.dropna(subset=['Runtime', 'Genre'], inplace=True)

data['Genre'] = data['Genre'].str.split(', ')

all_genres = set(g for sublist in data['Genre'] for g in sublist)
genre_to_index = {genre: idx for idx, genre in enumerate(all_genres)}

def encode_genres(genres):
    encoded = np.zeros(len(all_genres))
    for genre in genres:
        if genre in genre_to_index:
            encoded[genre_to_index[genre]] = 1
    return encoded

data['Genre_Encoding'] = data['Genre'].apply(encode_genres)


data['Released_Year'] = pd.to_numeric(data['Released_Year'], errors='coerce')
data = data.dropna(subset=['Released_Year']) 

X = np.hstack([
    data[['Released_Year', 'Runtime']].values,
    np.array(list(data['Genre_Encoding']))
])

y = data['IMDB_Rating'].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

knn = NearestNeighbors(n_neighbors=5, algorithm='auto')
knn.fit(X_train)

def get_nearest_neighbors_features(features, k=5):
    distances, indices = knn.kneighbors(features, n_neighbors=k)
    return indices

def predict_movie_ratings(test_features, k=5):
    predicted_ratings = []
    for feature in test_features:
        feature = feature.reshape(1, -1) 
        neighbors_indices = get_nearest_neighbors_features(feature, k)
        neighbor_ratings = np.mean([y_train[indices] for indices in neighbors_indices], axis=0)
        predicted_ratings.append(np.mean(neighbor_ratings))
    return np.array(predicted_ratings)

y_pred = predict_movie_ratings(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")


def recommend_movie(user_input):
    user_genres_encoded = encode_genres(user_input['genre'])
    user_features = np.array([
        user_input['year'],
        user_input['runtime'],
        *user_genres_encoded
    ]).reshape(1, -1)

    user_features_scaled = scaler.transform(user_features)

    distances, indices = knn.kneighbors(user_features_scaled)

    recommended_movies = data.iloc[indices[0]]
    return recommended_movies[['Series_Title', 'IMDB_Rating','Certificate','Runtime']]

# static input for testing
# user_input = {
#     'year': 2010,
#     'genre': ['Comedy', 'Drama', 'Family'],
#     'runtime': 120
# }

# recommended_movies = recommend_movie(user_input)
# print("Recommended Movies:")
# print(recommended_movies)