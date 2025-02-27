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
        f.write('Este top nacional esta basado en SPOTIFY. No incluye cuentas de productores solo artistas ya sean solitarios, dupla o grupos. Si deseas aparecer pasame tu ID por mis redes sociales:\n')
        f.write('<a href="https://www.facebook.com/KvnDuran" target="_blank"><img src="https://static.vecteezy.com/system/resources/previews/017/221/797/large_2x/facebook-logo-transparent-background-free-png.png" alt="Facebook" style="width:30px;height:30px;margin-right:10px;">Kvn Durán</a>\n')
        f.write('<a href="https://www.instagram.com/kvn_duran" target="_blank"><img src="https://static.vecteezy.com/system/resources/previews/017/743/717/large_2x/instagram-icon-logo-free-png.png" alt="Instagram" style="width:30px;height:30px;margin-left:10px;">@kvn_duran</a>\n')
        f.write('<table>\n')
        f.write('  <tr>\n')
        f.write('    <th>Top</th>\n')
        f.write('    <th>Foto de Perfil</th>\n')
        f.write('    <th>Nombre</th>\n')
        f.write('    <th>Popularidad</th>\n')
        f.write('    <th>Seguidores</th>\n')
        f.write('    <th>Género</th>\n')
        f.write('    <th>Perfil de Spotify</th>\n')
        f.write('  </tr>\n')

        for index, artist in enumerate(sorted_artists, start=1):
            name = artist['name']
            popularity = artist['popularity']
            followers = artist['followers_total']
            spotify_url = artist['spotify_url']
            image_url = artist['images'][0]['url']  # Tomamos la imagen de mayor calidad
            genres = ', '.join(artist['genres'])  # Géneros del artista

            # Asignar estilo según el puesto
            if index == 1:
                row_style = 'background-color: rgba(255, 215, 0, 0.3);'  # Oro
            elif index == 2:
                row_style = 'background-color: rgba(192, 192, 192, 0.3);'  # Plata
            elif index == 3:
                row_style = 'background-color: rgba(205, 127, 50, 0.3);'  # Bronce
            elif 4 <= index <= 10:
                row_style = 'background-color: rgba(205, 127, 50, 0.1);'  # Bronce más tenue
            else:
                row_style = ''  # Sin estilo para puestos mayores a 10

            f.write(f'  <tr style="{row_style}">\n')  # Aplicar estilo inline
            f.write(f'    <td>{index}</td>\n')
            f.write(f'    <td><img src="{image_url}" alt="{name}" width="100"></td>\n')
            f.write(f'    <td>{name}</td>\n')
            f.write(f'    <td>{popularity}</td>\n')
            f.write(f'    <td>{followers}</td>\n')
            f.write(f'    <td>{genres}</td>\n')
            f.write(f'    <td><a href="{spotify_url}" target="_blank">Ir a su Spotify</a></td>\n')
            f.write('  </tr>\n')

        f.write('</table>\n')



if __name__ == '__main__':
    artists_data = load_data('../data/top_rappers.json')
    generate_markdown(artists_data, '../ranking.md')
