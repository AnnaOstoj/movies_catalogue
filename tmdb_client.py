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

def get_movies_list(list_type="popular"):
    url = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()

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
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    r = requests.get(url, headers=headers)
    return r.json()

def get_single_movie_cast(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    r = requests.get(url, headers=headers)
    return r.json()["cast"]

def get_single_movie_images(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    r = requests.get(url, headers=headers)
    return r.json()["backdrops"]

def search_movie(search_query):
    url = f"https://api.themoviedb.org/3/search/movie/?query={search_query}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    r = requests.get(url, headers=headers)
    return r.json()

def get_airing_today():
    url = f"https://api.themoviedb.org/3/tv/airing_today"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    r = requests.get(url, headers=headers)
    return r.json()