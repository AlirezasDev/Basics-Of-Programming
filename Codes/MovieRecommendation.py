watched_movies = eval(input())
movie_genres = eval(input())
preferred_genres = eval(input())

recommendations = {}

for user in watched_movies:
    user_preferred_genres = preferred_genres.get(user, set())
    user_watched_movies = set(watched_movies.get(user, []))
    recommended_movies = []

    for movie, genres in movie_genres.items():
        if movie not in user_watched_movies and genres.intersection(user_preferred_genres):
            recommended_movies.append(movie)

    recommendations[user] = sorted(recommended_movies, reverse=True)

for user in sorted(recommendations.keys()):
    movies = ', '.join(recommendations[user])
    print(f"{user}: {movies}")
