from unittest.mock import Mock
import tmdb_client


def test_get_poster_url_uses_default_size():
   # Przygotowanie danych
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Wywołanie kodu, który testujemy
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Porównanie wyników
   assert expected_default_size in poster_url

"""
def test_get_movies_list(monkeypatch):
    # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    response = requests_mock.return_value
    # Przysłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)


    movies_list = tc.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list


def test_get_single_movie_title(monkeypatch):
    mock_movie_title = {"title": "Harry Potter and the Philosopher's Stone"}
    my_mock = Mock()
    my_mock.return_value = mock_movie_title

    monkeypatch.setattr("tc.get_single_movie.requests.get", my_mock)

    movie = tc.get_single_movie(movie_id = 'tt0241527')

    assert movie['title'] == mock_movie_title['title']

def test_get_single_movie_endpoint(monkeypatch):
    mock_movie_endpoint = "movie/671"
    my_mock = Mock()
    my_mock.return_value = mock_movie_endpoint
    monkeypatch.setattr("tc.get_single_movie.request.base_url", my_mock)

    movie = tc.get_single_movie.request.base_url
    assert mock_movie_endpoint in movie
 
def test_get_movie_images(monkeypatch):
    pass
        
def test_get_single_movie_cast(monkeypatch):
    pass
"""