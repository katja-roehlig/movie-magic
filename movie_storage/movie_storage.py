import json

# with open("movies.json", "w") as newfile:
#     json_string = json.dumps(main.movies, indent=4)
#     newfile.write(json_string)


def get_movies():
    """
    Returns a list of dictionaries that
    contains the movie information.
    The function loads the information from the JSON
    file and returns the data.
    """
    try:
        with open("movies.json", "r") as data:
            movies = json.loads(data.read())
            return movies
    except FileNotFoundError as e:
        print(e)


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open("movies.json", "w") as newfile:
        json_string = json.dumps(movies, indent=4)
        newfile.write(json_string)


def add_movie(movies, title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """

    new_movie = {"title": title, "year of release": year, "rating": rating}
    movies.append(new_movie)
    save_movies(movies)


def delete_movie(movies, index):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """

    del movies[index]
    save_movies(movies)


def update_movie(movies, index, title, year, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies[index] = {"title": title, "year of release": year, "rating": rating}
    save_movies(movies)
