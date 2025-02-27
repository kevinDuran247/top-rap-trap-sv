import json

# Leer los datos desde el JSON
def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# Generar el contenido en formato Markdown con tabla HTML
def generate_markdown(artists, output_file): 
    # Ordenar los artistas por el número de seguidores de mayor a menor
    sorted_artists = sorted(artists, key=lambda x: x['followers_total'], reverse=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('# Top Raperos/Traperos de El Salvador 🎶🇸🇻\n\n')
        f.write('<table>\n')
        f.write('  <tr>\n')
        f.write('    <th>Foto de Perfil</th>\n')  # Nueva columna para la foto antes del nombre
        f.write('    <th>Nombre</th>\n')
        f.write('    <th>Popularidad</th>\n')
        f.write('    <th>Seguidores</th>\n')
        f.write('    <th>Género</th>\n')  # Nueva columna para el género
        f.write('    <th>Canción más escuchada</th>\n')  # Nueva columna para la canción más escuchada
        f.write('    <th>Creacion de la cuenta</th>\n')  # Nueva columna para la fecha de creación
        f.write('    <th>Perfil de Spotify</th>\n')
        f.write('  </tr>\n')

        for artist in sorted_artists:
            name = artist['name']
            popularity = artist['popularity']
            followers = artist['followers_total']
            spotify_url = artist['spotify_url']
            image_url = artist['images'][0]['url']  # Tomamos la imagen de mayor calidad
            genres = ', '.join(artist['genres'])  # Géneros del artista
            top_track = artist['top_track'] if artist['top_track'] else 'No disponible'  # Canción más escuchada
            creation_date = artist['creation_date']  # Fecha de creación del artista

            f.write('  <tr>\n')
            f.write(f'    <td><img src="{image_url}" alt="{name}" width="100"></td>\n')  # Foto de perfil
            f.write(f'    <td>{name}</td>\n')
            f.write(f'    <td>{popularity}</td>\n')
            f.write(f'    <td>{followers}</td>\n')
            f.write(f'    <td>{genres}</td>\n')  # Género
            f.write(f'    <td>{top_track}</td>\n')  # Canción más escuchada
            f.write(f'    <td>{creation_date}</td>\n')  # Fecha de creación
            f.write(f'    <td><a href="{spotify_url}" target="_blank">Ir a su Spotify</a></td>\n')
            f.write('  </tr>\n')

        f.write('</table>\n')



if __name__ == '__main__':
    artists_data = load_data('../data/top_rappers.json')
    generate_markdown(artists_data, '../ranking.md')
