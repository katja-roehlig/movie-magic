# 🪄 MovieMagic

MovieMagic is a Python-based tool that helps you build and manage your own personal movie database. Instead of typing everything manually, it fetches all the details like release years, ratings, and posters directly from the **OMDb API**.

I built this project to keep track of my movies, get some cool stats, and even generate a nice-looking website to show off the collection.

## 🚀 Features

The app runs in your console with an easy-to-use menu. Here’s what you can do:

*   **Smart Search & Add:** Just type a movie title, and the app grabs the data from OMDb.
*   **Manage Your List:** Update ratings or delete movies you no longer like.
*   **Stats & Insights:** Get the average and median ratings, or see your best and worst-rated films.
*   **Visuals:** Create a **rating histogram** to see how your taste is distributed.
*   **Random Picker:** Can't decide what to watch? Let the "Random Movie" function choose for you.
*   **Filter & Sort:** Sort your collection by year or rating, or use filters to find specific movies.
*   **Web Generator:** With one click, the app turns your database into a clean **HTML website**.

## 🛠️ Tech Stack

*   **Python:** The core of the project.
*   **SQLite & SQLAlchemy:** To store and manage the movie data safely.
*   **OMDb API:** To get all the movie information and posters.
*   **HTML/Jinja:** For generating the web view.

## 📦 Setup

1. **Clone the project:**
   ```bash
   git clone https://github.com/katja-roehlig/movie-magic.git

2. **Install requirements:**
   ```bash
   pip install -r requirements.txt

3. **API Key:**
   Create a .env file in the main folder and add your OMDb API key like this:
   API_KEY=your_key_here

4. **Run it:**
   ```bash
   python.main.py

## 📝 About this Project

This was a fun project to learn more about APIs, databases, and Python. It combines a classic console interface with modern features like SQL-storage and web generation. Feel free to check it out!

