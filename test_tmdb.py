from unittest.mock import Mock
import tmdb_client as tc
import pytest
from main import app

# zadanie 2

def test_homepage(monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client: # co się tutaj dzieje? w podobny sposób trzeba by przetestować endopoint poniżej?
       response = client.get('/movie/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/popular') # co robi ta linia?


@pytest.mark.parametrize("test_input", ("popular", "upcoming"))
def test_homepage_list(monkeypatch, test_input):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get(f'/movie/?list_type={test_input}')
        print(response)
        assert response.status_code == 200

# zadanie 1

def test_get_single_movie_title(monkeypatch):
    mock_movie_title = {"title": "Harry Potter and the Philosopher's Stone"}
    my_mock = Mock()
    response = my_mock.return_value
    response.json.return_value = mock_movie_title
    monkeypatch.setattr("tmdb_client.requests.get", my_mock)
    movie = tc.get_single_movie(movie_id = '671')

    assert movie['title'] == mock_movie_title['title']

"""
def test_get_single_movie_endpoint(monkeypatch):
    mock_movie_endpoint = "movie/671"
    my_mock = Mock()
    response = my_mock.return_value
    response.url.return_value = mock_movie_endpoint
    monkeypatch.__setattr__("tmdb_client.response.url", my_mock)

    movie = tc.get_single_movie(movie_id = '671')
    assert mock_movie_endpoint in movie.url  # movie nie ma atrybutu url... jak wyciągnąć endpoint?

def test_get_single_movie_images(monkeypatch):
    mock_movie_image_file_path = {'file_path': '/4GlSMUpzSd3cliYGFJVziSDX53S.jpg'}
    
    my_mock = Mock()
    response = my_mock.return_value
    response.json.return_value = mock_movie_image_file_path
    monkeypatch.setattr("tmdb_client.requests.get", my_mock)
    
    movie_images = tc.get_single_movie_images(movie_id = 671)

    assert type(movie_images[0]['file_path']) == str


def test_get_single_movie_cast(monkeypatch):
    mock_movie_actor = 'Daniel Radcliffe'
    
    my_mock = Mock()
    response = my_mock.return_value
    response.json.return_value = mock_movie_actor
    monkeypatch.setattr("tmdb_client.requests.get", my_mock)
    
    movie_cast = tc.get_single_movie_cast(movie_id = 671)

    assert movie_cast[0]['name'] == mock_movie_actor

"""