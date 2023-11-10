# app/routes.py
from flask import render_template
from app import app
from app.src.services.tmdb_service import TMDbService

tmdb_api_key = 'fde60adbf95d59157f5c7b5c84607e0c'  # Reemplaza con tu clave de API de TMDb
tmdb_service = TMDbService(api_key=tmdb_api_key)

@app.route('/')
def index():
    # Obtener detalles de una película (reemplaza movie_id con el ID de la película que estás interesado)
    movie_id = '552'
    movie_details = tmdb_service.get_movie_details(movie_id)

    if movie_details:
        # Construir la URL del póster
        poster_path = movie_details['poster_path']
        poster_url = tmdb_service.build_poster_url(poster_path)
        return render_template('index.html', movie_details=movie_details, poster_url=poster_url)
    else:
        return render_template('index.html', error_message='No se pudieron obtener detalles de la película.')
