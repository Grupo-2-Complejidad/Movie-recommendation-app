# app/services/tmdb_service.py
import requests


class TMDbService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.themoviedb.org/3/'
        self.image_base_url = 'https://image.tmdb.org/t/p/'

    def get_movie_details(self, movie_id):
        endpoint = f'movie/{movie_id}'
        url = f'{self.base_url}{endpoint}?api_key={self.api_key}'

        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def build_poster_url(self, poster_path, size='w500'):
        return f'{self.image_base_url}{size}{poster_path}'
