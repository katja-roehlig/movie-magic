import movie_storage.movie_storage_sql as storage


def get_html_string_for_one_movie(movie):
    """
    Takes a dictionary and generates a string with HTML elements from specific data within it.
    :param movie -  dictionary
    :return string for one movie
    """
    output = ""
    title, year, rating, img_url = movie
    alternative_url = (
        "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"
    )
    output += f"""
                <li class='movie'>
                    <div class='img-container'>
                        <img src='{img_url},
                        alt='Movie Image'
                        class='movie-poster'
                        onerror='this.onerror=null;this.src=\"{alternative_url}\";'/>
                        <div class='rating-container'>
                        <img src='star.svg' alt='Stern-Icon' width='60' height='60' class='star'/>
                        <div class='movie-rating'>{rating}</div>
                        </div>
                    </div>
                <div class='movie-title'>{title}</div>
                <div class='movie-year'>{year}</div>
               
                </li>
                """
    return output


def get_html_string_for_all_movies(movie_list):
    """
    Generates a string with HTML elements from all dictionaries in a list.
    return: string for all movies
    """
    movies_string = ""
    for movie in movie_list:
        movies_string += get_html_string_for_one_movie(movie)
    return movies_string


def create_new_html_page(html_string):
    """
    Replaces text from the HTML file with a string and saves the page in a new HTML page
    """
    web_title = "MY MOVIE APP"
    with open("_static/index_template.html", "r") as page_file:
        web_data = page_file.read()
    new_web_data = web_data.replace(" __TEMPLATE_MOVIE_GRID__", html_string).replace(
        "__TEMPLATE_TITLE__", web_title
    )
    with open("_static/index.html", "w") as new_file:
        new_file.write(new_web_data)


def generate_web_page():
    """
    takes the movie list and turns it into a website
    """
    movie_list = storage.show_movie_list()
    movies_string = get_html_string_for_all_movies(movie_list)
    create_new_html_page(movies_string)
    print("The website was successfully generated!")


if __name__ == "__main__":
    generate_web_page()
