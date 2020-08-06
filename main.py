from flask import Flask, render_template, request
import tmdb_client as tc
from random import sample, randrange

app = Flask(__name__)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tc.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route('/movie/')
def homepage():
    movies_list = ["upcoming", "top_rated", "popular", "now_playing"]
    data = request.args.get('list_type', "upcoming")
    if data in movies_list:
        movies = tc.get_movies(how_many=8, list_type=data)
        return render_template("homepage.html", movies=movies, current_list=movies, lists=movies_list)
    else:
        movies = tc.get_movies(how_many=8, list_type="popular")
        return render_template("homepage.html", movies=movies, current_list=movies, lists=movies_list)

@app.route('/movie/<movie_id>')
def movie_details(movie_id):
    movie = tc.get_single_movie(movie_id)
    cast = tc.get_single_movie_cast(movie_id)[:8]
    images = tc.get_single_movie_images(movie_id)
    random_image = sample(images, 1)
    image_url = random_image[0]['file_path']
    return render_template("movie_details.html", movie=movie, cast=cast, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)