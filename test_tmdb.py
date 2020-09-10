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

   with app.test_client() as client: 
       response = client.get('/movie/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/popular') 

def test_homepage_template():

   with app.test_client() as client: 
       response = client.get('/movie/')
       assert bytes("Witaj w mojej bibliotece filmów", 'utf-8') in response.data

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

upcoming_movies = [{'popularity': 2068.491, 'vote_count': 35, 'video': False, 'poster_path': '/9Rj8l6gElLpRL7Kj17iZhrT5Zuw.jpg', 'id': 734309, 'adult': False, 
                    'backdrop_path': '/7fvdg211A2L0mHddvzyArRuRalp.jpg', 'original_language': 'en', 'original_title': 'Santana', 'genre_ids': [28], 'title': 'Santana', 'vote_average': 5.9, 
                    'overview': 'Two brothers — one a narcotics agent and the other a general — finally discover the identity of the drug lord who murdered their parents decades ago. They may kill'+ 
                    'each other before capturing the bad guys.', 'release_date': '2020-08-28'}, {'popularity': 1653.138, 'vote_count': 1078, 'video': False, 'poster_path':
                    '/aKx1ARwG55zZ0GpRvU2WrGrCG9o.jpg', 'id': 337401, 'adult': False, 'backdrop_path': '/xl5oCFLVMo4d4Pgxvrf8Jmc2IlA.jpg', 'original_language': 'en', 'original_title':
                    'Mulan', 'genre_ids': [28, 12, 18, 14, 10752], 'title': 'Mulan', 'vote_average': 7.8, 'overview': 'When the Emperor of China issues a decree that one man per family must'+ 
                    'serve in the Imperial Chinese Army to defend the country from Huns, Hua Mulan, the eldest daughter of an honored warrior, steps in to take the place of her ailing father.'+ 
                    'She is spirited, determined and quick on her feet. Disguised as a man by the name of Hua Jun, she is tested every step of the way and must harness her innermost strength and'+ 
                    'embrace her true potential.', 'release_date': '2020-09-04'}, {'popularity': 1577.352, 'vote_count': 111, 'video': False, 'poster_path': '/sMO1v5TUf8GOJHbJieDXsgWT2Ud.jpg', 
                    'id': 438396, 'adult': False, 'backdrop_path': '/qGZe9qTuydxyJYQ60XDtEckzLR8.jpg', 'original_language': 'es', 'original_title': 'Orígenes secretos', 'genre_ids': [18, 53], 
                    'title': 'Unknown Origins', 'vote_average': 6.2, 'overview': 'In Madrid, Spain, a mysterious serial killer ruthlessly murders his victims by recreating the first appearance of'+ 
                    'several comic book superheroes. Cosme, a veteran police inspector who is about to retire, works on the case along with the tormented inspector David Valentín'+
                    'and his own son Jorge Elías, a nerdy young man who owns a comic book store.', 'release_date': '2020-08-28'}, {'popularity': 1535.066, 'vote_count': 24, 'video': False, 
                    'poster_path': '/ugZW8ocsrfgI95pnQ7wrmKDxIe.jpg', 'id': 724989, 'adult': False, 'backdrop_path': '/86L8wqGMDbwURPni2t7FQ0nDjsH.jpg', 'original_language': 'en', 
                    'original_title': 'Hard Kill', 'genre_ids': [28, 53], 'title': 'Hard Kill', 'vote_average': 5.3, 'overview': 'The work of billionaire tech CEO Donovan Chalmers is so valuable'+
                    'that he hires mercenaries to protect it, and a terrorist group kidnaps his daughter just to get it.', 'release_date': '2020-08-25'}, {'popularity': 1236.635, 
                    'vote_count': 162, 'video': False, 'poster_path': '/zVncJzXzwIO15YM1WilqYn30r54.jpg', 'id': 718444, 'adult': False, 'backdrop_path': '/x4UkhIQuHIJyeeOTdcbZ3t3gBSa.jpg', 
                    'original_language': 'en', 'original_title': 'Rogue', 'genre_ids': [28], 'title': 'Rogue', 'vote_average': 6, 'overview': 'Battle-hardened O’Hara leads a lively mercenary team'+ 
                    'of soldiers on a daring mission: rescue hostages from their captors in remote Africa. But as the mission goes awry and the team is stranded, O’Hara’s squad must face a bloody,'+ 
                    'brutal encounter with a gang of rebels.', 'release_date': '2020-08-20'}, {'popularity': 841.906, 'vote_count': 365, 'video': False, 'poster_path': '/sy6DvAu72kjoseZEjocnm2ZZ09i.jpg',
                        'id': 581392, 'adult': False, 'backdrop_path': '/gEjNlhZhyHeto6Fy5wWy5Uk3A9D.jpg', 'original_language': 'ko', 'original_title': '반도', 'genre_ids': [28, 27, 53], 
                        'title': 'Peninsula', 'vote_average': 7.2, 'overview': 'A soldier and his team battle hordes of post-apocalyptic zombies in the wastelands of the Korean Peninsula', 
                        'release_date': '2020-07-15'}, {'popularity': 841.67, 'vote_count': 1123, 'video': False, 'poster_path': '/TnOeov4w0sTtV2gqICqIxVi74V.jpg', 'id': 605116, 'adult': False, 
                        'backdrop_path': '/qVygtf2vU15L2yKS4Ke44U4oMdD.jpg', 'original_language': 'en', 'original_title': 'Project Power', 'genre_ids': [28, 80, 878], 'title': 'Project Power', 
                        'vote_average': 6.7, 'overview': 'An ex-soldier, a teen and a cop collide in New Orleans as they hunt for the source behind a dangerous new pill that grants users temporary'+ 
                        'superpowers.', 'release_date': '2020-08-14'}, {'popularity': 840.907, 'vote_count': 181, 'video': False, 'poster_path': '/tM4hht0LdY06UbuxGR4LjK6adCD.jpg', 'id': 613504, 
                        'adult': False, 'backdrop_path': '/dZJJDmiwp0W1NE74SY5WV00v0Ec.jpg', 'original_language': 'en', 'original_title': 'After We Collided', 'genre_ids': [18, 10749], 
                        'title': 'After We Collided', 'vote_average': 7.2, 'overview': 'Tessa finds herself struggling with her complicated'+ 
                    'relationship with Hardin; she faces a dilemma that could change their lives forever.', 'release_date': '2020-09-02'}]

def test_get_movies_list_upcoming_length(monkeypatch):
    my_mock = Mock()
    response = my_mock.return_value
    response.json.return_value = upcoming_movies
    monkeypatch.setattr("tmdb_client.requests.get", my_mock)
    movies = tc.call_tmdb_api("movie/?list_type=upcoming")
    assert len(movies) == len(upcoming_movies)

single_movie_images = {'id': 613504, 'backdrops': [{'aspect_ratio': 1.777777777777778, 'file_path': '/dZJJDmiwp0W1NE74SY5WV00v0Ec.jpg', 'height': 2160, 'iso_639_1': 'fr', 
                    'vote_average': 0.0, 'vote_count': 0, 'width': 3840}, {'aspect_ratio': 1.777777777777778, 'file_path': '/r5srC0cqU36n38azFnCyReEksiR.jpg', 'height': 2160, 'iso_639_1': None, 
                    'vote_average': 0.0, 'vote_count': 0, 'width': 3840}], 'posters': [{'aspect_ratio': 0.6665120593692022, 'file_path': '/t3euf9hyvr9avWxKF4iJYvct0MK.jpg', 'height': 2156, 
                    'iso_639_1': 'fr', 'vote_average': 5.384, 'vote_count': 2, 'width': 1437}, {'aspect_ratio': 0.68, 'file_path': '/tM4hht0LdY06UbuxGR4LjK6adCD.jpg', 'height': 1000, 'iso_639_1': 'en', 
                    'vote_average': 5.318, 'vote_count': 3, 'width': 680}, {'aspect_ratio': 0.6666666666666666, 'file_path': '/3k4TvOWxJZyeMJtbjHQELKIEhpb.jpg', 'height': 3000, 'iso_639_1': 'es', 
                    'vote_average': 5.246, 'vote_count': 2, 'width': 2000}, {'aspect_ratio': 0.6666666666666666, 'file_path': '/5pg2rn4SM47B6Orc1xWXZ3MAVUc.jpg', 'height': 1500, 'iso_639_1': 'es', 
                    'vote_average': 5.246, 'vote_count': 2, 'width': 1000}, {'aspect_ratio': 0.6665443873807777, 'file_path': '/ijcykNO87JLCgxUltTFqHwlK2yT.jpg', 'height': 2726, 'iso_639_1': 'en', 
                    'vote_average': 5.246, 'vote_count': 2, 'width': 1817}, {'aspect_ratio': 0.6664913203577064, 'file_path': '/bGMAZEVNdBkPV1JAnXqXGIcgRkF.jpg', 'height': 1901, 'iso_639_1': 'fr', 
                    'vote_average': 5.172, 'vote_count': 1, 'width': 1267}, {'aspect_ratio': 0.6664915966386554, 'file_path': '/siXfS57rM6CjX7uivtASokTdm8M.jpg', 'height': 1904, 'iso_639_1': 'fr', 
                    'vote_average': 5.172, 'vote_count': 1, 'width': 1269}, {'aspect_ratio': 0.6668568168853394, 'file_path': '/8erUtl8ySBo4ywO1GUEvIQCwP6j.jpg', 'height': 1753, 'iso_639_1': 'fr', 
                    'vote_average': 5.172, 'vote_count': 1, 'width': 1169}, {'aspect_ratio': 0.6749156355455568, 'file_path': '/d2K5l98Z5VwTMqH7wT3YaOuLOnJ.jpg', 'height': 889, 'iso_639_1': 'es', 
                    'vote_average': 5.172, 'vote_count': 1, 'width': 600}, {'aspect_ratio': 0.6666666666666666, 'file_path': '/7Zhv1JBcCmP8cf6mcbAYmnrgiIu.jpg', 'height': 3000, 'iso_639_1': 'en', 
                    'vote_average': 0.0, 'vote_count': 0, 'width': 2000}, {'aspect_ratio': 0.6706349206349206, 'file_path': '/d45gDeSa3eDpYo2Aj6AJ7SeHx0t.jpg', 'height': 2268, 'iso_639_1': 'ko', 
                    'vote_average': 0.0, 'vote_count': 0, 'width': 1521}, {'aspect_ratio': 0.6666666666666666, 'file_path': '/do1qoZsWxLo0XcDILZqip6wSNZC.jpg', 'height': 750, 'iso_639_1': 'hu', 
                    'vote_average': 0.0, 'vote_count': 0, 'width': 500}, {'aspect_ratio': 0.6666666666666666, 'file_path': '/uqwppvYo4rHqDeDbHVQD4Q8jXIu.jpg', 'height': 3000, 'iso_639_1': 'cs', 
                    'vote_average': 0.0, 'vote_count': 0, 'width': 2000}, {'aspect_ratio': 0.6666666666666666, 'file_path': '/k5XhOQmWchldax6bI5VGucfdR5X.jpg', 'height': 3000, 'iso_639_1': 'sv', 
                    'vote_average': 0.0, 'vote_count': 0, 'width': 2000}, {'aspect_ratio': 0.66640625, 'file_path': '/jFhE8XqXt8F8IGZuiBmY3z9bGS5.jpg', 'height': 1280, 'iso_639_1': 'uk', 
                    'vote_average': 0.0, 'vote_count': 0, 'width': 853}, {'aspect_ratio': 0.6666666666666666, 'file_path': '/auGR1XgvuOB5oFvpY7DMUEjxgyt.jpg', 'height': 750, 'iso_639_1': 'it', 
                    'vote_average': 0.0, 'vote_count': 0, 'width': 500}]}

def test_get_single_movie_images(monkeypatch):
    my_mock = Mock()
    response = my_mock.return_value
    response.json.return_value = single_movie_images
    monkeypatch.setattr("tmdb_client.requests.get", my_mock)
    movie_images = tc.get_single_movie_images(613504)
    assert movie_images["backdrops"] == single_movie_images["backdrops"]

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


def test_get_single_movie_images_2(monkeypatch):
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

