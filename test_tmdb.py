from unittest.mock import Mock
import tmdb_client as tc
import pytest
from main import app
import requests

# zadanie 2
"""
def test_homepage(monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client: # co się tutaj dzieje? w podobny sposób trzeba by przetestować endopoint poniżej?
       response = client.get('/movie/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/popular') # po co nm ta linia?


@pytest.mark.parametrize("test_input", ("popular", "upcoming"))
def test_homepage_list(monkeypatch, test_input):
    api_mock = Mock(return_value=[{'popularity': 2037.113, 'vote_count': 153, 'video': False, 'poster_path': '/zVncJzXzwIO15YM1WilqYn30r54.jpg', 'id': 718444, 
                                'adult': False, 'backdrop_path': '/x4UkhIQuHIJyeeOTdcbZ3t3gBSa.jpg', 'original_language': 'en', 'original_title': 'Rogue',
                                'genre_ids': [28], 'title': 'Rogue', 'vote_average': 6, 'overview': 'Battle-hardened O’Hara leads a lively mercenary team of soldiers on a daring'+ 
                                'mission: rescue hostages from their captors in remote Africa. But as the mission goes awry and the team is stranded, O’Hara’s squad must face a bloody,'+
                                'brutal encounter with a gang of rebels.', 'release_date': '2020-08-20'}, {'popularity': 1465.301, 'vote_count': 1087, 'video': False, 'poster_path': 
                                '/TnOeov4w0sTtV2gqICqIxVi74V.jpg', 'id': 605116, 'adult': False, 'backdrop_path': '/qVygtf2vU15L2yKS4Ke44U4oMdD.jpg', 
                                'original_language': 'en', 'original_title': 'Project Power', 'genre_ids': [28, 80, 878], 'title': 'Project Power', 'vote_average': 6.7, 
                                'overview': 'An ex-soldier, a teen and a cop collide in New Orleans as they hunt for the source behind a dangerous new pill that grants users'+ 
                                'temporary superpowers.', 'release_date': '2020-08-14'}])

    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get('/movie/')
        assert response['title'] == api_mock['title']
"""
# zadanie 1

def test_get_single_movie_title(monkeypatch):
    mock_movie_title = {"title": "Harry Potter and the Philosopher's Stone"}
    my_mock = Mock()
    response = my_mock.return_value
    response.json.return_value = mock_movie_title
    monkeypatch.setattr("tmdb_client.requests.get", my_mock)
    movie = tc.get_single_movie(movie_id = '671')

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
    
    movie_images = tc.get_single_movie_images(movie_id = 671)

    assert movie_images['file_path'] == mock_movie_image_file_path['file_path']


def test_get_single_movie_cast(monkeypatch):
    mock_movie_actor = {'name':'Daniel Radcliffe'}
    
    my_mock = Mock()
    response = my_mock.return_value
    response.json.return_value = mock_movie_actor
    monkeypatch.setattr("tmdb_client.requests.get", my_mock)
    
    movie_cast = tc.get_single_movie_cast(movie_id = 671)

    assert movie_cast['name'] == mock_movie_actor['name']

