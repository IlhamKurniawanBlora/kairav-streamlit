import streamlit as st
import importlib
from pathlib import Path

# Inisialisasi posisi slide di dalam session_state
if 'slide_index' not in st.session_state:
    st.session_state.slide_index = 0

# Fungsi untuk menampilkan balon jika berada di slide pertama atau terakhir
def show_balloons():
    if st.session_state.slide_index == 0 or st.session_state.slide_index == len(slide_files) - 1:
        st.balloons()

# Load CSS file
css_path = Path("style.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Daftar nama file slide tanpa ekstensi `.py`
slide_files = [
    "slide1", "slide2", "slide3", "slide4", "slide5",
    "slide6", "slide7", "slide8", "slide9", "slide10"
]

# Fungsi untuk navigasi slide
def go_previous():
    st.session_state.slide_index = max(0, st.session_state.slide_index - 1)

def go_next():
    st.session_state.slide_index = min(len(slide_files) - 1, st.session_state.slide_index + 1)

# Mendapatkan nama file slide saat ini
current_slide_file = slide_files[st.session_state.slide_index]

# Mengimpor dan menjalankan fungsi render dari file slide menggunakan importlib
slide_module = importlib.import_module(f"slides.{current_slide_file}")
slide_module.render()

# Menampilkan balon jika berada di slide 1 atau slide 10
show_balloons()

# Footer navigasi halaman dan tombol di bagian bawah
st.write(f"Slide {st.session_state.slide_index + 1} dari {len(slide_files)}")

# Tombol navigasi di bagian bawah
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("Back", key="prev_button"):
        go_previous()
with col3:
    if st.button("Next", key="next_button"):
        go_next()
