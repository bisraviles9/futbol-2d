from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).parent
st.set_page_config(page_title="Fútbol Arena 3D", page_icon="⚽", layout="wide")
st.markdown("""<style>
.block-container{padding-top:.6rem;padding-bottom:0;max-width:1200px}
header[data-testid="stHeader"],footer{visibility:hidden}
iframe{border:0}
</style>""", unsafe_allow_html=True)
st.title("⚽ Fútbol Arena 3D")
st.caption("Prototipo móvil 3D · 11 contra 11 · liga, copa, supercopa y torneo continental")
html = (ROOT / "index.html").read_text(encoding="utf-8")
three = (ROOT / "three.min.js").read_text(encoding="utf-8")
html = html.replace('<script src="./three.min.js"></script>', '<script>' + three + '</script>')
components.html(html, height=760, scrolling=False)
st.caption("Para instalarlo en Android o iPhone, abre la PWA publicada en GitHub Pages mientras tengas conexión; luego puedes añadirla a la pantalla de inicio.")
