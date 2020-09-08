from unittest.mock import Mock
import tmdb_client as tc
import pytest
from main import app
import requests
import flask

# zadanie 2

        #  przykład z modułu
def test_homepage(monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client: # co się tutaj dzieje? w podobny sposób trzeba by przetestować endopoint poniżej?
       response = client.get('/movie/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/popular') # po co nm ta linia? żeby wywołać tylko jeden request get?


@pytest.mark.parametrize("test_input", ("popular", "upcoming"))
def test_homepage_2(monkeypatch, test_input):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get(f'movie/?list_type={test_input}')
        api_mock.assert_called_once_with(f'movie/{test_input}')
        assert response.status_code == 200


@pytest.mark.parametrize("test_input", ("popular", "upcoming"))
def test_homepage_list_1(test_input):

    with app.test_request_context(f'/movie/{test_input}'):
        assert flask.request.path == f"/movie/{test_input}"


@pytest.mark.parametrize("test_input", ("popular", "upcoming"))
def test_homepage_list_2(monkeypatch, test_input):
    mock_movies_list = [{'title': 'Movie1'}, {'title': 'Movie2'}]
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tc.get_movies_list(list_type=test_input)
    assert movies_list == mock_movies_list



# zadanie 1


def test_get_single_movie_title(monkeypatch):
    mock_movie_title = {"title": "Harry Potter and the Philosopher's Stone"}
    my_mock = Mock()
    response = my_mock.return_value
    response.json.return_value = mock_movie_title
    monkeypatch.setattr("tmdb_client.requests.get", my_mock)
    movie = tc.call_tmdb_api("movie/671")

    assert movie['title'] == mock_movie_title['title']

def test_get_single_movie_title_2():
    response = requests.get('https://api.themoviedb.org/3/movie/tt0241527?api_key=b8f9ad59b4a4643aad3607578073a94a&language=en-US')
    response_body = response.json()
    assert response_body['title'] == 'Harry Potter and the Philosopher\'s Stone'


def test_get_single_movie_images(monkeypatch):
    mock_movie_image_file_path = {'file_path': '/4GlSMUpzSd3cliYGFJVziSDX53S.jpg'}
    
    my_mock = Mock()
    response = my_mock.return_value
    response.json.return_value= mock_movie_image_file_path
    monkeypatch.setattr("tmdb_client.requests.get", my_mock)
    
    movie_images = tc.call_tmdb_api("movie/671/images")

    assert movie_images['file_path'] == mock_movie_image_file_path['file_path']


def test_get_single_movie_cast(monkeypatch):
    mock_movie_actor = {'name':'Daniel Radcliffe'}
    
    my_mock = Mock()
    response = my_mock.return_value
    response.json.return_value = mock_movie_actor
    monkeypatch.setattr("tmdb_client.requests.get", my_mock)
    
    movie_cast = tc.call_tmdb_api("movie/671/credits")

    assert movie_cast['name'] == mock_movie_actor['name']

