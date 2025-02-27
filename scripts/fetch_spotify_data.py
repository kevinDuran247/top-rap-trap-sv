import requests
import json
import os
from dotenv import load_dotenv

# Credenciales de la app de Spotify
load_dotenv()

CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

# Lista de IDs de artistas salvadoreños
artist_ids = [
    '0CJa1b77vpBYM017HMLgAu',
    '0JsMrE7jf2ynuVoVXaXxF3',
    '7Gq0ss88YMxOkKkh7DaKV5',
    '1BidZUckyWcn6zqbhl0lhm'
]

# Autenticación y obtención de token de acceso
def get_spotify_token():
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    })
    auth_data = auth_response.json()
    return auth_data['access_token']

# Obtener información detallada de un artista por su ID
def get_artist_info(token, artist_id):
    artist_url = f'https://api.spotify.com/v1/artists/{artist_id}'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(artist_url, headers=headers)
    return response.json()

# Guardar información relevante de los artistas en un archivo JSON
def save_artists_info(token, artist_ids):
    artists_info = []
    for artist_id in artist_ids:
        artist_data = get_artist_info(token, artist_id)
        
        # Obtener el género del artista
        genres = artist_data.get('genres', [])
        
        # Obtener la canción más escuchada (Top Track)
        top_track = artist_data.get('tracks', [])[0] if 'tracks' in artist_data else None
        top_track_name = top_track.get('name') if top_track else None
        
        # Obtener la fecha de creación del artista (esto puede estar disponible dependiendo de la API)
        # Spotify no proporciona directamente la fecha de creación del artista, pero se puede aproximar
        # a través del primer álbum o el primer track en su historial.
        creation_date = artist_data.get('followers', {}).get('created_at', 'Fecha no disponible')
        
        info = {
            'name': artist_data.get('name'),
            'popularity': artist_data.get('popularity'),
            'followers_total': artist_data['followers'].get('total'),
            'spotify_url': artist_data['external_urls'].get('spotify'),
            'images': artist_data.get('images'),
            'genres': genres,
            'top_track': top_track_name,
            'creation_date': creation_date
        }
        artists_info.append(info)

    with open('../data/top_rappers.json', 'w', encoding='utf-8') as f:
        json.dump(artists_info, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    token = get_spotify_token()
    save_artists_info(token, artist_ids)
