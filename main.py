from flask import Flask, render_template, request, url_for, redirect, flash
import tmdb_client as tc
from random import sample, randrange
import datetime
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

FAVORITES = set()

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tc.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route('/movie/')
def homepage():
    movies_list = ["upcoming", "top_rated", "popular", "now_playing", "favorites"]
    data = request.args.get('list_type', "popular")
    if data in movies_list:
        if data == "favorites":
            return redirect(url_for('show_favorites'))
        else:
            movies = tc.get_movies(how_many=8, list_type=data)
            print(movies)
            return render_template("homepage.html", movies=movies, current_list=movies, lists=movies_list, active = data)
    else:
        movies = tc.get_movies(how_many=8, list_type="popular")
        return render_template("homepage.html", movies=movies, current_list=movies, lists=movies_list)

@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    movie = tc.get_single_movie(movie_id)
    cast = tc.get_single_movie_cast(movie_id)["cast"][:8]
    images = tc.get_single_movie_images(movie_id)["backdrops"]
    random_image = sample(images, 1)
    image_url = random_image[0]['file_path']
    return render_template("movie_details.html", movie=movie, cast=cast, image_url=image_url)

@app.route('/movie/search', methods=['GET'])
def search():
    search_query = request.args.get("search_query", "")
    if search_query:
        data = tc.search_movie(search_query=search_query)
        movies = data['results']
    else:
        movies = []
    return render_template("search.html", movies=movies, search_query=search_query)

@app.route('/movie/today')
def airing_today():
    data = tc.get_airing_today()
    movies = data['results']
    today = datetime.date.today()
    return render_template("airing.html", movies=movies, today=today)

@app.route('/movie/favorites/add', methods=['POST'])
def add_to_favorites():
    movie_id = request.form.get("movie_id", "")
    if movie_id:
        FAVORITES.add(movie_id)
        movie = tc.get_single_movie(movie_id)
        movie_title = movie["title"]
        flash(f'Dodano film {movie_title} do listy ulubionych')
    return redirect(url_for('homepage'))

@app.route('/movie/favorites/')
def show_favorites():
    movies_list = ["upcoming", "top_rated", "popular", "now_playing", "favorites"]
    movies = []
    for i in FAVORITES:
        movie = tc.get_single_movie(i)
        movies.append(movie)
    return render_template("homepage.html", movies=movies, current_list=movies, lists=movies_list)

if __name__ == '__main__':
    app.run(debug=True)