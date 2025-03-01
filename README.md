# 🎶 Top Raperos/Traperos de El Salvador

![Top Artistas de El Salvador](portada.jpg)

Este proyecto presenta un ranking de los principales artistas de rap y trap en El Salvador, basado en datos obtenidos directamente desde la API de Spotify. El objetivo es destacar a los talentos locales y mostrar información como su popularidad, cantidad de seguidores y enlace directo a su perfil en Spotify.


## 🚀 Cómo Ejecutar

### 1. Clonar el repositorio
```bash
git clone https://github.com/kevinDuran247/top-rap-trap-sv
```

### 2. Configurar las credenciales de la API de Spotify
Crea un archivo `.env` en la raíz del proyecto:
```env
SPOTIFY_CLIENT_ID=tu_client_id_aqui
SPOTIFY_CLIENT_SECRET=tu_client_secret_aqui
```
Asegúrate de no subir este archivo al repositorio.

### 5. Obtener datos de Spotify
```bash
python scripts/fetch_spotify_data.py
```

### 6. Generar el archivo Markdown
```bash
python scripts/generate_markdown.py
```

## 📄 Resultado Final
El archivo `ranking.md` contendrá una tabla HTML ordenada por número de seguidores, mostrando:

- **Foto del perfil** del artista
- **Nombre** del artista
- **Nivel de popularidad** (0-100)
- **Cantidad de seguidores**
- **Enlace directo** a su perfil de Spotify

## 📝 Contribuciones
¿Conoces más raperos o traperos salvadoreños? ¡Haz un PR y ayúdanos a ampliar esta lista!

## 📄 Licencia
Este proyecto está bajo la licencia MIT.

