# Fútbol 2D

Juego arcade original de fútbol, inspirado en los videojuegos clásicos. Incluye equipos ficticios, opción Ecuador vs. Brasil, controles táctiles, IA básica, marcador y partidos rápidos. No utiliza marcas, escudos ni recursos de PES/Konami.

## Streamlit

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

En Streamlit Community Cloud selecciona este repositorio y `app.py` como archivo principal. La versión Streamlit necesita internet.

## Jugar sin conexión en el teléfono

Los archivos `index.html`, `manifest.webmanifest`, `sw.js` e `icon.svg` forman una PWA. Publica el repositorio como sitio GitHub Pages usando la rama `main` y carpeta raíz. Abre el sitio una vez con conexión y añádelo a la pantalla de inicio (Android: menú del navegador; iPhone: Compartir → Añadir a pantalla de inicio). Luego puede jugarse offline. La primera carga e instalación sí requieren internet.

## Controles

- Móvil: joystick y botones SELEC., BARRER, ROBAR y PRESS.
- PC: WASD/flechas, espacio para chutar, X para pase, Escape para pausa.
