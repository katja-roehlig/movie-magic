QUERY_CREATE_TABLE = """
                    CREATE TABLE IF NOT EXISTS movies(
                    id INTEGER PRIMARY KEY,
                    title TEXT UNIQUE NOT NULL,
                    year INTEGER NOT NULL,
                    rating REAL NOT NULL,
                    image TEXT NOT NULL
                    )
                    """

QUERY_ADD_MOVIE = """
                INSERT INTO movies(
                title, year, rating, image)
                VALUEs(
                :title, :year,:rating, :image)
                """

QUERY_UPDATE_MOVIE = """
                    UPDATE movies
                    SET year = :year, rating = :rating
                    WHERE title = :title
                    """

QUERY_DELETE_MOVIE = """
                    DELETE FROM movies
                    WHERE title = :title
                    """
QUERY_SHOW_ALL = """
                SELECT title, year, rating, image FROM movies
                """
QUERY_GET_TITLE = """
                SELECT * FROM movies
                WHERE title = :title
                    """
QUERY_BEST_FILM = """
                SELECT * FROM movies
                WHERE rating = (SELECT MAX(rating) FROM movies)
                """
QUERY_WORST_FILM = """
                SELECT * FROM movies
                WHERE rating = (SELECT MIN(rating) FROM movies)
                """
QUERY_AVG_RATING = """SELECT AVG(rating) FROM movies"""

QUERY_ALL_RATINGS = """ SELECT rating FROM movies"""

QUERY_RANDOM_MOVIE = """SELECT title, year, rating 
                        FROM movies
                        ORDER BY RANDOM()
                        LIMIT 1
                    """
QUERY_SEARCH = """
            SELECT title, year, rating
            FROM movies
            WHERE title LIKE :search
             """

QUERY_ALL_SORTED_BY_RATING = """
                            SELECT title, year, rating
                            FROM movies
                            ORDER BY rating DESC
                            """

QUERY_SORTED_BY_YEAR_ASC = """
                            SELECT title, year, rating
                            FROM movies
                            ORDER BY year ASC
                            """
QUERY_SORTED_BY_YEAR_DESC = """
                            SELECT title, year, rating
                            FROM movies
                            ORDER BY year DESC
                            """
QUERY_FILTER = """
                SELECT title, year, rating
                FROM movies
                WHERE year BETWEEN :start AND :end AND rating > :rating
                """
