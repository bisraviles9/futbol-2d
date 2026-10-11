from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Fútbol 2D", page_icon="⚽", layout="wide")
st.markdown("""<style>
  .block-container {padding-top: .7rem; padding-bottom: 0; max-width: 1200px}
  header[data-testid="stHeader"], footer {visibility:hidden}
  iframe {border:0}
</style>""", unsafe_allow_html=True)
st.title("⚽ Fútbol 2D")
st.caption("Partido arcade original · controles táctiles y teclado · versión web")
html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=760, scrolling=False)
st.caption("Para jugar sin conexión, instala la versión PWA desde su página estática de GitHub Pages mientras tengas internet.")
