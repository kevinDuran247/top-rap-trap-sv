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
    '1BidZUckyWcn6zqbhl0lhm',
    '3Fzx6lDy4x8VFhPsu3LVuD',
    '1HY2aGDLtIADXBkpiyTbyH',
    '2zUs5mMJkZwn0XKHKglBME',
    '2vBCXtOB46hkU6YvLtSVz2',
    '595vJ3WnQb5qAbifBAS8UQ',
    '2IBiHiiKi0YFt77E0gEyAm',
    '7mwHFG3zdvlFphf1CXFwWf',
    '3QvLhQoURAFBZjNnOAgjzl',
    '7FARTpburrayzgBudPcQTB',
    '3Bqi9hqSNMPoicjvz8j2jm',
    '2bJN3vGQsLrGqgzwRMluQY',
    '6KOSNc6cyaAjs7hh379tZ2',
    '6j2N8MgI7tFi4SwUIFevQ9',
    '31wtY2T6lHi77pV9RsVTqm'
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
        
        info = {
            'name': artist_data.get('name'),
            'popularity': artist_data.get('popularity'),
            'followers_total': artist_data['followers'].get('total'),
            'spotify_url': artist_data['external_urls'].get('spotify'),
            'images': artist_data.get('images'),
            'genres': genres
        }
        artists_info.append(info)

    with open('../data/top_rappers.json', 'w', encoding='utf-8') as f:
        json.dump(artists_info, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    token = get_spotify_token()
    save_artists_info(token, artist_ids)
