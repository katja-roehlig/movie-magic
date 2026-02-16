from sqlalchemy import create_engine, text
import queries


DB_URL = "sqlite:///data/movies.db"

engine = create_engine(DB_URL, echo=False)


def create_query(query, params=None):
    if params is None:
        params = {}
    try:
        with engine.connect() as connection:
            connection.execute(text(query), params)
            connection.commit()
            return True

    except Exception as e:
        print("Query error:", e)
        return False


def execute_query(query, params=None):
    if params is None:
        params = {}
    try:
        with engine.connect() as connection:
            results = connection.execute(text(query), params)
            return results.fetchall()
    except Exception as e:
        print("Query error:", e)
        return []


def create_basic_table():
    """
    Creates basic database table
    """
    if create_query(queries.QUERY_CREATE_TABLE):
        print("Database successfully created")


def add_movie(title, year, rating, image):
    """
    adds a movie to the database
    :params title, year, rating, image
    """
    params = {"title": title, "year": year, "rating": rating, "image": image}
    return create_query(queries.QUERY_ADD_MOVIE, params=params)


def update_movie(title, year, rating):
    """
    updates a mvie in the database
    :params title, year, rating
    """
    params = {"title": title, "year": year, "rating": rating}
    return create_query(queries.QUERY_UPDATE_MOVIE, params=params)


def delete_movie(title):
    """
    deletes a movie in the database
    :param title
    """
    params = {"title": title}
    return create_query(queries.QUERY_DELETE_MOVIE, params=params)


def show_movie_list():
    """
    get movie list form database
    """
    return execute_query(queries.QUERY_SHOW_ALL)


def get_movie_by_title(title):
    """
    get a movie by title from database
    :param title
    """
    params = {"title": title}
    return execute_query(queries.QUERY_GET_TITLE, params)


def get_average_rating():
    """
    get average of all movie ratings
    """
    return execute_query(queries.QUERY_AVG_RATING)


def get_best_movies():
    """
    get the best movies from database
    """
    return execute_query(queries.QUERY_BEST_FILM)


def get_worst_movies():
    """
    get the worst movies from database
    """
    return execute_query(queries.QUERY_WORST_FILM)


def get_all_ratings():
    """
    get all given ratings from database
    """
    return execute_query(queries.QUERY_ALL_RATINGS)


def get_random_movie():
    """
    get a random movie from database
    """
    return execute_query(queries.QUERY_RANDOM_MOVIE)


def get_search_results(search):
    """
    get all result from user-search from database
    :param search
    """
    params = {"search": f"%{search}%"}
    return execute_query(queries.QUERY_SEARCH, params=params)


def get_all_sorted_by_rating():
    """
    get all movies sorted by rating from database
    """
    return execute_query(queries.QUERY_ALL_SORTED_BY_RATING)


def get_sorted_by_year(choice):
    """
    get all movies sorted by rating from database
    :param choice: asc odr desc
    """
    if choice == "y":
        return execute_query(queries.QUERY_SORTED_BY_YEAR_DESC)
    else:
        return execute_query(queries.QUERY_SORTED_BY_YEAR_ASC)


def filter_by_year_and_rating(start, end, rating):
    """filters all movies by year and rating"""
    params = {"start": start, "end": end, "rating": rating}
    return execute_query(queries.QUERY_FILTER, params=params)
