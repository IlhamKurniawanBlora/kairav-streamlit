import streamlit as st
from PIL import Image

# Load image
img = Image.open("kairav.png")  # Pastikan gambar "kairav.png" ada di folder proyekmu

# Tampilan gambar dan judul
st.image(img, width=200)
st.title("Portofolio Ilham Kurniawan")

# Pengenalan
st.header("Tentang Saya")
st.write(
    """
    Saya Ilham Kurniawan, seorang mahasiswa jurusan Informatika dengan minat kuat pada pengembangan perangkat lunak, khususnya di bidang web development dan data analysis.  
    Selama beberapa tahun terakhir, saya telah mengasah keterampilan saya dalam bahasa Python dan teknologi terkait untuk menghasilkan solusi yang efisien dan inovatif.
    """
)

# Skill dengan logo
st.header("Skill Saya di Bidang IT")
col1, col2, col3 = st.columns(3)

# Skill 1
with col1:
    st.image("python-logo.png", width=50)  # Logo Python
    st.write("Python")

# Skill 2
with col2:
    st.image("streamlit-logo.png", width=50)  # Logo Streamlit
    st.write("Streamlit")

# Skill 3
with col3:
    st.image("html-logo.png", width=50)  # Logo HTML
    st.write("HTML & CSS")

# Contact
st.header("Kontak")
st.write(
    """
    Jika Anda tertarik untuk bekerja sama atau ingin mengenal lebih lanjut tentang proyek-proyek saya, jangan ragu untuk menghubungi saya!
    """
)
st.write("Email: ilham@example.com")
