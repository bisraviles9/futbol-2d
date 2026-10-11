# Fútbol Arena 3D

Prototipo de fútbol web en 3D ligero para Android/iPhone, con 11 jugadores por equipo, controles táctiles, IA básica y cuatro formatos jugables: Liga, Copa, Supercopa y Copa de Campeones (fase de grupos y eliminatorias, inspirada en el formato Champions). Los equipos y escudos son ficticios; no contiene licencias oficiales.

## Ejecutar en Streamlit

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

Streamlit incorpora la biblioteca Three.js desde el archivo local `three.min.js`.

## Instalar en el teléfono

Abre el sitio HTTPS de GitHub Pages una vez con internet y elige **Añadir a pantalla de inicio** / **Instalar aplicación**. El juego precarga los archivos necesarios para abrirse offline después de esa primera descarga. Gira el teléfono a horizontal durante los partidos.

## Torneos en esta versión

- Liga Nacional: ida y vuelta (14 partidos del equipo jugador).
- Copa Nacional: cuartos, semifinal y final.
- Supercopa: final a partido único.
- Copa de Campeones: grupo, semifinal y final si se clasifica.

Los modos guardan el progreso en el almacenamiento local del navegador. Three.js está distribuido bajo licencia MIT; consulta `THREE_LICENSE.txt`.
