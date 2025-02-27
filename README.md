# 🎶 Top Raperos/Traperos de El Salvador

![Top Artistas de El Salvador](top-artistas.png)

Este proyecto presenta un ranking de los principales artistas de rap y trap en El Salvador, basado en datos obtenidos directamente desde la API de Spotify. El objetivo es destacar a los talentos locales y mostrar información como su popularidad, cantidad de seguidores y enlace directo a su perfil en Spotify.


## 🚀 Cómo Ejecutar

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/spotify-top-artists.git
cd spotify-top-artists
```

### 2. Crear un entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar las credenciales de la API de Spotify
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

