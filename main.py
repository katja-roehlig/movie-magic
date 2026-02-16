import statistics
import matplotlib.pyplot as plt
from movie_storage import movie_storage_sql as storage
import api.api_handler as req
import generating_webpage as webpage


def handle_exit():
    """
    Says Bye and quits the program
    """
    print("Bye")
    return False


def show_menu_and_get_user_input(functions_dict):
    """
    Displays the menu and asks for user action
    :return: user action
    """
    print("***** My Movies Database *****\n \nMenu:")
    print("Menu:")
    for key, value in functions_dict.items():
        print(f"{key}. {value[1]}")
    while True:
        try:
            user_action = int(input("\nEnter choice (0-11): "))
            if user_action in functions_dict:
                return user_action
            else:
                print("Not a valid number!")
                continue
        except ValueError:
            print("That was not a number! Enter a number!")


def show_movies():
    """
    Displays all entries in the film ddatabase and their ratings in no particular order
    """
    movie_list = storage.show_movie_list()
    print(f"\n{len(movie_list)} movies in total")
    for movie in movie_list:
        print(f"{movie.title} ({movie.year}): {movie.rating}")


def get_year(text):
    """
    Asks the user after one year and validates the answer
    :param text: The question for the user
    :return: year
    """
    while True:
        year = input(text)
        if year == "":
            return None
        try:
            year = int(year)
            if 1900 < year < 2100:
                return year
            print("Please enter a valid year ")
        except ValueError:
            print("Please enter a valid year ")


def get_rating(text):
    """
    Asks the user after a rating and validates the answer
    :param text: The question for the user
    :return: rating
    """
    while True:
        rating = input(text)
        if rating == "":
            return None
        try:
            rating = float(rating)
            if 0 <= rating <= 10:
                return rating
            print("Rating must be a number between 0 and 10: ")
        except ValueError:
            print("Please enter a valid rating ")


def add_movie():
    """
    Adds an entry to the movie database
    """
    while True:
        movie_name = input("Enter new movie name: ")
        if movie_name.strip():
            break
        print("Enter a movie title: ")
    movie = storage.get_movie_by_title(movie_name)
    if movie:
        print("Movie already exists!")
        return
    result = req.get_movie_info_per_title(movie_name)
    if result:
        title, year, rating, image = result
        if storage.add_movie(title, year, rating, image):
            print(f"Movie {movie_name} successfully added")
    elif result is False:
        print("Titel not found. Please try it with the titel in original language")
    else:
        print("Connection not available. Please try again later.")


def delete_movie():
    """
    Deletes an entry to the movie database
    """
    delete_movie_name = input("\nEnter movie name to delete: ").strip()
    if storage.delete_movie(delete_movie_name):
        print(f"Movie {delete_movie_name} successfully deleted")
    else:
        print("Ups, something went wrong. Try again.")


def update_movie():
    """
    Updates an entry in the movie_list
    """
    update_movie_name = input("\nEnter movie name: ").strip()
    movie = storage.get_movie_by_title(update_movie_name)
    if not movie:
        print(f"Movie {update_movie_name} does not exist")
        return
    else:
        release_year = get_year("Enter release year of the movie: ")
        rating = get_rating("Enter new movie rating (0-10): ")
        if storage.update_movie(update_movie_name, release_year, rating):
            print(f"Movie {update_movie_name} successfully updated.")
        else:
            print("Ups, something went wrong. Try again.")


def get_rating_list():
    """
    Generates a list from the movie ratings
    :return: list of ratings
    """
    result = storage.get_all_ratings()
    rating_list = [rating[0] for rating in result]
    return rating_list


def get_median():
    """
    Calculates the median of a list of numbers
    :return: median
    """
    list_of_numbers = get_rating_list()
    return round(statistics.median(list_of_numbers), 1)


def print_statistics():
    """
    Print the average, median, and best and worst entries.
    """
    avg_rating = storage.get_average_rating()
    print(f"\nAverage rating: {avg_rating[0][0]}")
    print(f"Median rating: {get_median()}")
    best_movie_list = storage.get_best_movies()
    for movie in best_movie_list:
        print(f"Best movie: {movie.title} ({movie.year}): {movie.rating}")

    worst_movie_list = storage.get_worst_movies()
    for movie in worst_movie_list:
        print(f"Best movie: {movie.title} ({movie.year}): {movie.rating}")


def choose_random_movie():
    """
    Selects an entry in a the database at random and prints it
    """
    random_list = storage.get_random_movie()
    if random_list:
        random_movie = random_list[0]
        print(
            f"\nYour movie for tonight: {random_movie.title}"
            f"({random_movie.year}) at range {random_movie.rating}"
        )
    else:
        print("Something went wrong. Please try again later")


def handle_user_search():
    """
    Searches entries for user-generated search terms in database and prints the result
    """
    user_search = input("\nEnter part of movie name: ").lower()
    if user_search in ("", " "):
        return
    movie_list = storage.get_search_results(user_search)
    if movie_list:
        for movie in movie_list:
            print(f"{movie.title} ({movie.year}), {movie.rating}")
    else:
        print("\nNo matching movies found!")


def get_movies_sorted_by_rating():
    """
    Sorts movies by values of the rating-key
    """
    rating_sorted_movie_list = storage.get_all_sorted_by_rating()
    for movie in rating_sorted_movie_list:
        print(f"{movie.title} ({movie.year}), {movie.rating}")


def get_movies_sorted_by_year():
    """
    Sorts movies by values of the year of release-key
    """
    while True:
        user_choice = input("Do you want the latest movies first? (Y/N) ").lower()
        if user_choice == "n" or "y":
            year_sorted_movie_list = storage.get_sorted_by_year(user_choice)
            for movie in year_sorted_movie_list:
                print(f"{movie.title} ({movie.year}), {movie.rating}")
            break
        else:
            print("Please enter 'Y' or 'N' ")


def filter_movies():
    """
    filters the movies by rating or time span and prints them
    :return:
    """
    min_rating = (
        get_rating("Enter minimum rating (leave blank for no minimum ranking): ") or 0
    )
    start_year = get_year("Enter start year (leave blank for no start year): ") or 0
    end_year = get_year("Enter end year (leave blank for no end year): ") or 9999

    filtered_movie_list = storage.filter_by_year_and_rating(
        start_year, end_year, min_rating
    )
    if filtered_movie_list:
        print()
        for movie in filtered_movie_list:
            print(f"{movie.title} ({movie.year}): {movie.rating}")
    else:
        print("No movie found")


def get_rating_histogram():
    """
    Creates a histogram and saves it if desired
    """
    data = get_rating_list()
    bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    plt.xticks(bins)
    plt.yticks(range(len(data)))
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    plt.grid(axis="y", alpha=0.5)
    plt.hist(
        data,
        bins=bins,
        density=False,
        cumulative=False,
        color="deeppink",
        edgecolor="black",
        alpha=0.4,
    )
    user_question = input("\nDo you want to safe the file? Type Y or N: ")
    if user_question == "Y":
        filename = input("Choose a name for the file (.png or .jpg): ")
        plt.savefig(filename)
    plt.show()


def main():
    """
    Interacts with the user and executes user actions
    """
    FUNCTIONS = {
        0: (handle_exit, "Exit"),
        1: (show_movies, "List movies"),
        2: (add_movie, "Add movie"),
        3: (delete_movie, "Delete movie"),
        4: (update_movie, "Update movie"),
        5: (print_statistics, "Statistics"),
        6: (choose_random_movie, "Random movie"),
        7: (handle_user_search, "Search movie"),
        8: (get_movies_sorted_by_rating, "Movies sorted by rating"),
        9: (get_movies_sorted_by_year, "Movies sorted by year"),
        10: (filter_movies, "Filter movies"),
        11: (webpage.generate_web_page, "Generate website"),
        12: (get_rating_histogram, "Create rating histogram"),
    }
    while True:
        user_input = show_menu_and_get_user_input(FUNCTIONS)
        print(user_input)
        choosen_action = FUNCTIONS[user_input][0]
        choosen_action()
        input("\nPress enter to continue")


if __name__ == "__main__":
    main()
