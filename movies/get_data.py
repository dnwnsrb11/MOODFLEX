import requests

API_KEY = 'cd8bc71b153e2ca169a6dca709dbb877'
BASE_URL = 'https://api.themoviedb.org/3'

def get_genres():
    # 영화 장르 목록 가져오기
    url = f"{BASE_URL}/genre/movie/list"
    params = {
        'api_key': API_KEY,
        'language': 'ko-KR',
    }
    response = requests.get(url, params=params)
    # HTTP 요청이 실패했을 때 예외를 발생시키는 코드
    response.raise_for_status()
    return response.json().get('genres', [])

def get_movies_by_genre(genre_id, page=1):
    # 해당 장르에 속한 영화 목록 가져오기
    url = f"{BASE_URL}/discover/movie"
    params = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'with_genres': genre_id,
        'page': page,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get('results', [])

def get_movie_details(movie_id):
    # 선택한 하나의 영화 상세 정보 가져오기
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        'api_key': API_KEY,
        'language': 'ko-KR',
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()



