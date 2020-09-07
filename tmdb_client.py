import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiOGY5YWQ1OWI0YTQ2NDNhYWQzNjA3NTc4MDczYTk0YSIsInN1YiI6IjVmMmE1Njg1NGI2ZDlkMDAzNDgyYzc3ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.JMr6EpASsMk-1FCoDyOH3DmPaMMKQnjsJGxIT78Tbkw"

"""
def get_popular_movies():
    url = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    r = requests.get(url, headers=headers)
    return r.json()
"""
def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_movies_list(list_type="popular"):
    return call_tmdb_api(f"movie/{list_type}")

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_poster_url(poster_url, poster_size = "w342"):
    base_url = "https://image.tmdb.org/t/p"
    return  f"{base_url}/{poster_size}/{poster_url}"


def get_movie_info(movies):
    movies_list = []
    for i in movies:
        movies_list.append({"title": i["title"], "poster_path": i["poster_path"]})
    return movies_list

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

def get_single_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits")

def get_single_movie_images(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/images")

def search_movie(search_query):
    return call_tmdb_api(f"search/movie/?query={search_query}")

def get_airing_today():
    return call_tmdb_api(f"tv/airing_today")